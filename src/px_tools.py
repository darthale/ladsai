from typing import List
import prometheux_chain as pmtx
import re
import random

from src.openai_api import get_client
from src.utils import get_logger, fetch_prompt_config

USE_CASE_1_GET_STARTUPS_VADA = "data/vadalog/use_case_1/get_startups.vada"
USE_CASE_1_GET_OUTPUT_VADA = "data/vadalog/use_case_1/get_output_use_case_1.vada"
USE_CASE_1_GET_EXPLANATION_VADA = "data/vadalog/use_case_1/get_explanation_use_case_1.vada"
PROMPT_CONFIG_PATH = ["src/prompts/angel_summary_01.txt", "integration_tests/use_case_1/angel_summary_01.txt"]

client = get_client()
logger = get_logger()
EXPLAIN_ANGEL_RECOMMENDATION_PROMPT = fetch_prompt_config(PROMPT_CONFIG_PATH)

# Add at the top of the file with other global variables
current_suggestions = {}

def recommend_angels_for_company(company_name: str) -> str:
    global current_suggestions
    # here we make the call to Prometheux API via the SDKS
    logger.info(f"Recommend angels for company: {company_name}")
    facts = pmtx.perform(USE_CASE_1_GET_OUTPUT_VADA, {"startup": company_name, "degree_of_separation":"3"})

    # Convert Facts to strings
    fact_strings = [str(fact) for fact in facts]
    selected_facts = fact_strings[:20]
    
    # Clear previous suggestions and create new mapping
    current_suggestions.clear()
    for fact in selected_facts:
        # Extract angel name using regex (assumes format: startup_angel_suggestion(Company|Angel|type|score))
        if match := re.search(r'startup_angel_suggestion\([^|]+\|([^|]+)\|', fact):
            angel_name = match.group(1)
            current_suggestions[angel_name] = fact
    
    # Join with newlines
    return "\n".join(selected_facts)
    
def fetch_available_startups() -> str:
    # here we make the call to Prometheux API via the SDKS
    logger.info(f"Fetching available startups..")
    startups = pmtx.perform(USE_CASE_1_GET_STARTUPS_VADA)

    # Extract startup names using regex
    startup_names = [re.search(r'startup_name\((.*?)\)', str(s)).group(1) for s in startups]
    
    # Get random sample of 30 (or less if there are fewer startups)
    sample_size = min(30, len(startup_names))
    random_startups = random.sample(startup_names, sample_size)
    print(f"Random startups: {random_startups}")
    
    return "\n".join(random_startups)

def explain_recommend_angel(user_explanation_choice: str) -> str:
    # here we make a call to a chat completion endpoint to summarize Prometheux output
    logger.info(f"Fetchin explanation for {user_explanation_choice}")

    full_explanation_key = current_suggestions[user_explanation_choice]
    # explanation = pmtx.perform(USE_CASE_1_GET_EXPLANATION_VADA, {"fact_to_explain": full_explanation_key})
    explanation = pmtx.perform(USE_CASE_1_GET_EXPLANATION_VADA, {"fact_to_explain": full_explanation_key})
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": EXPLAIN_ANGEL_RECOMMENDATION_PROMPT},
            {"role": "user", "content": explanation[0].get_arg_by_pos(1)}],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    logger.info(f"Summarized explanation response: {response}")
    
    return response.choices[0].message.content    

def connection_with_person_x(person_name: str) -> str:
    # here we make the call to Prometheux API via the SDKS
    print(f"Connection with person: {person_name}")
    return "This connection is important because..."

tools = [{
    "type": "function",
    "function": {
        "name": "recommend_angels_for_company",
        "description": "Recommend angels for a company. Call this whenever you need to recommend angels for a company. For example, when a user asks 'Which angels could be a good fit for this company?'",
        "parameters": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "The company name to recommend angels for."
                }
            },
            "required": ["company_name"],
            "additionalProperties": False
        } 
        }
},
{
    "type": "function",
    "function": {
        "name": "connection_with_person_x",
        "description": "Get a connection with a person. Call this whenever you need to get a connection with a person. For example, when a user asks 'Who is the connection with person X?'",
        "parameters": {
            "type": "object",
            "properties": {
                "person_name": {
                    "type": "string",
                    "description": "The person name to get a connection with."
                }
            },
            "required": ["person_name"],
            "additionalProperties": False
        }}
},
{
    "type": "function",
    "function": {
        "name": "fetch_available_startups",
        "description": "Fetch the list of the available startups in the system. Call this whenever you need to get a list of startups the user can interact with. For example, when a user asks 'What startups are available to me today for analysis?'",
     }
},
{
    "type": "function",
    "function": {
        "name": "explain_recommend_angel",
        "description": "Given a recommended angel, explain in lay-terms why this angel was recommended. Call this whenever you need to get a human explanation. For example, when a user asks 'Tell me why this angel was recommended?'",
        "parameters": {
            "type": "object",
            "properties": {
                "user_explanation_choice": {
                    "type": "string",
                    "description": "The explanation choice made by the user."
                }
            },
            "required": ["user_explanation_choice"],
            "additionalProperties": False
        }
     }
}
]
