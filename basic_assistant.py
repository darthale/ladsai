from openai import OpenAI
from src.px_tools import tools, recommend_angels_for_company,connection_with_person_x
import json
import time

client = OpenAI()

assistant = client.beta.assistants.create(
    name="VC Platform Manager Assistant",
    instructions="You are a seasoned Venture Capitalist Platform Manager. You are responsible for finding and managing the relationships between the fund partner and their network. Adapt your language based on your role and think as a platform manager. Use the provided functions to answer questions when needed. Synthesise answer based on provided function output and be consise",
    tools=tools,
    model="gpt-4o-mini"
)


def get_function_details(run):

  print("\nrun.required_action\n",run.required_action)

  function_name = run.required_action.submit_tool_outputs.tool_calls[0].function.name
  arguments = run.required_action.submit_tool_outputs.tool_calls[0].function.arguments
  function_id = run.required_action.submit_tool_outputs.tool_calls[0].id

  print(f"function_name: {function_name} and arguments: {arguments}")

  return function_name, arguments, function_id

def create_message_and_run(assistant,query,thread=None):
  if not thread:
    thread = client.beta.threads.create()

  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=query
  )
  run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
  )
  return run,thread

def submit_tool_outputs(run,thread,function_id,function_response):
    run = client.beta.threads.runs.submit_tool_outputs(
    thread_id=thread.id,
    run_id=run.id,
    tool_outputs=[
      {
        "tool_call_id": function_id,
        "output": str(function_response),
      }
    ]
    ) 
    return run

available_functions = {
    "recommend_angels_for_company": recommend_angels_for_company,
    "connection_with_person_x": connection_with_person_x,
}


def execute_function_call(function_name,arguments):
    function = available_functions.get(function_name,None)
    if function:
        arguments = json.loads(arguments)
        results = function(**arguments)
    else:
        results = f"Error: function {function_name} does not exist"
    return results

query = "I want to know the path that I can use to connect to " 
run,thread = create_message_and_run(assistant=assistant,query=query)


while True:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print("run status", run.status)

    if run.status=="requires_action":

        function_name, arguments, function_id  = get_function_details(run)

        function_response = execute_function_call(function_name,arguments)

        run = submit_tool_outputs(run,thread,function_id,function_response)

        continue
    if run.status=="completed":

        messages = client.beta.threads.messages.list(thread_id=thread.id)
        latest_message = messages.data[0]
        text = latest_message.content[0].text.value
        print(text)

        user_input = input()
        if user_input == "STOP":
          break

        run,thread = create_message_and_run(assistant=assistant,query=user_input,thread=thread)

        continue;
    time.sleep(1)

