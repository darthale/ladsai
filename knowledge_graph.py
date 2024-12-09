import os
import io
import queue
import json
from dotenv import load_dotenv  # Add this import
load_dotenv()

import streamlit as st
from openai import OpenAI
from streamlit import session_state as ss
from PIL import Image

from src.px_tools import recommend_angels_for_company, \
                        explain_recommend_angel, fetch_available_startups, display_network_graph, \
                        recommend_experts_for_company, explain_recommend_expert, tools, get_shortest_path_sources_targets
from src.utils import get_logger
from src.openai_api import get_client

logger = get_logger()

available_functions = {
    "recommend_angels_for_company": recommend_angels_for_company,
    "fetch_available_startups": fetch_available_startups,
    "explain_recommend_angel": explain_recommend_angel,
    "display_network_graph": display_network_graph,
    "recommend_experts_for_company": recommend_experts_for_company,
    "explain_recommend_expert": explain_recommend_expert,
    "get_shortest_path_sources_targets": get_shortest_path_sources_targets
}
client = get_client()
ASSISTANT_PROMPT = open("src/prompts/assistant.txt", "r").read()

st.cache_resource(show_spinner=False)

def your_knowledge_graph():

    if 'tool_requests' not in ss:
        ss['tool_requests'] = queue.Queue()
    tool_requests = ss['tool_requests']


    def get_function_details(tool):

        logger.info(f"\n run.required_action {tool} \n")

        function_name = tool.function.name
        arguments = tool.function.arguments
        function_id = tool.id

        logger.info(f"function_name: {function_name} and arguments: {arguments}")

        return function_name, arguments, function_id

    def execute_function_call(function_name,arguments):
        function = available_functions.get(function_name,None)
        if function:
            arguments = json.loads(arguments)
            results = function(**arguments)
        else:
            results = f"Error: function {function_name} does not exist"
        return results

    def handle_requires_action(tool_request):
        st.toast("Running a function", icon=":material/function:")
        tool_outputs = []
        data = tool_request.data
        for tool in data.required_action.submit_tool_outputs.tool_calls:

            function_name, function_arguments, function_id  = get_function_details(tool)
            logger.info(f"Calling the function {function_name} with arguments {function_arguments}")
            function_response = execute_function_call(function_name, function_arguments)
            tool_outputs.append({"tool_call_id": tool.id, "output": function_response})
        
        logger.info("Function invocation completed")    
        st.toast("Function completed", icon=":material/function:")
        return tool_outputs, data.thread_id, data.id

    def data_streamer():
        """
        Stream data from the assistant. Text messages are yielded. Images and tool requests are put in the queue.
        :return:
        :rtype:
        """
        logger.info(f"Starting data streamer on {ss.stream}")
        st.toast("Thinking...", icon=":material/emoji_objects:")
        content_produced = False
        for response in ss.stream:
            match response.event:
                case "thread.message.delta":
                    content = response.data.delta.content[0]
                    match content.type:
                        case "text":
                            value = content.text.value
                            content_produced = True
                            yield value
                        case "image_file":
                            logger.info(f"Image file: {content}")
                            image_content = io.BytesIO(client.files.content(content.image_file.file_id).read())
                            content_produced = True
                            yield Image.open(image_content)
                case "thread.run.requires_action":
                    logger.info(f"Run requires action: {response}")
                    tool_requests.put(response)
                    if not content_produced:
                        yield "Reasoning through the knowledge graph whilst inferring properties.."
                    return
                case "thread.run.failed":
                    logger.error(f"Run failed: {response}")
                    return
        st.toast("Completed", icon=":material/emoji_objects:")
        logger.info(f"Finished data streamer on {ss.stream}")

    def add_message_to_state_session(message):
        if len(message) > 0:
            ss.messages.append({"role": "assistant", "content": message})


    def display_stream(content_stream, create_context=True):
        ss.stream = content_stream
        if create_context:
            with st.chat_message("assistant"):
                response = st.write_stream(data_streamer)
        else:
            response = st.write_stream(data_streamer)
        if response is not None:
            if isinstance(response, list):
                # Multiple messages in the response
                for message in response:
                    add_message_to_state_session(message)
            else:
                # Single message in response
                add_message_to_state_session(response)

    def run():
        if "assistant" not in ss:
            assistant = client.beta.assistants.create(
                name="Venture Capitalist Platform Manager Assistant",
                instructions=ASSISTANT_PROMPT,
                model="gpt-4o",
                tools = tools
            )

            if assistant is None:
                raise RuntimeError(f"Assistant not found.")
            logger.info(f"Located assistant: {assistant.name}")
            ss["assistant"] = assistant
        assistant = ss["assistant"]

        if "messages" not in st.session_state:
            ss.messages = []

        # Display chat messages from state session on streamlit
        for message in ss.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        if prompt := st.chat_input("Ask the assistant"):
            # Display user message and add to history
            with st.chat_message("user"):
                st.write(prompt)
            ss.messages.append({"role": "user", "content": prompt})

            # Create a new thread if not already created
            if 'thread' in ss:
                thread = ss['thread']
            else:
                thread = client.beta.threads.create()
                logger.info(f"Created new thread: {thread.id}")
                ss['thread'] = thread

            # Add user message to the thread
            client.beta.threads.messages.create(thread_id=thread.id,
                                                role="user",
                                                content=prompt)

            # Create a new run with stream
            with client.beta.threads.runs.stream(
                    thread_id=thread.id,
                    assistant_id=assistant.id
            ) as stream:
                # Start writing assistant messages to chat
                display_stream(stream)
                while not tool_requests.empty():
                    logger.info("Handling tool requests")
                    with st.chat_message("assistant"):
                        tool_outputs, thread_id, run_id = handle_requires_action(tool_requests.get())
                        logger.info(f"Tool outputs: {tool_outputs}")
                        with client.beta.threads.runs.submit_tool_outputs_stream(
                                thread_id=thread_id,
                                run_id=run_id,
                                tool_outputs=tool_outputs
                        ) as tool_stream:
                            display_stream(tool_stream, create_context=False)


    run()