import prometheux_chain as pmtx
import re
import random
import streamlit as st
from streamlit_agraph import agraph, Config, Node, Edge
import json
from typing import Dict, List

from src.openai_api import get_client
from src.utils import get_logger, fetch_prompt_config

USE_CASE_1_GET_STARTUPS_VADA = "data/vadalog/use_case_1/get_startups.vada"
USE_CASE_1_ANGEL_GET_OUTPUT_VADA = "data/vadalog/use_case_1/angel/get_output_startups_angels_suggestions.vada"
USE_CASE_1_ANGEL_GET_EXPLANATION_VADA = "data/vadalog/use_case_1/angel/get_explanation_startups_angels_suggestions.vada"
USE_CASE_1_EXPERT_GET_OUTPUT_SUGGESTION_VADA = "data/vadalog/use_case_1/expert/get_output_startups_experts_suggestions.vada"
USE_CASE_1_EXPERT_GET_EXPLANATION_SUGGESTION_VADA = "data/vadalog/use_case_1/expert/get_explanation_startups_experts_suggestions.vada"

USE_CASE_2_GET_EXPLANATION_PEOPLE_OR_FUNDS_PROPERTIES_OVERLAPS_VADA = "data/vadalog/use_case_2/get_explanation_people_or_funds_properties_overlaps.vada"
USE_CASE_2_EXPLAIN_PEOPLE_OR_FUNDS_PROPERTIES_OVERLAPS = "data/vadalog/use_case_2/explain_people_or_funds_properties_overlaps.vada"
USE_CASE_2_GET_FUND_TOP_TIER_PROPERTY_OVERLAP_LIST_VADA = "data/vadalog/use_case_2/get_fund_top_tier_property_overlap.vada"
USE_CASE_2_GET_PEOPLE_OR_FUNDS_PROPERTIES_OVERLAPS_VADA = "data/vadalog/use_case_2/get_people_or_funds_properties_overlaps.vada"
USE_CASE_2_GET_PEOPLE_TYPES_PROPERTIES_OVERLAPS_PERCENTAGES_VADA = "data/vadalog/use_case_2/get_people_types_properties_overlaps_percentages.vada" 
USE_CASE_2_INDEX_EXPLANATIONS_PEOPLE_OR_FUNDS_PROPERTIES_OVERLAPS_VADA = "data/vadalog/use_case_2/index_explanations_people_or_funds_properties_overlaps.vada"
USE_CASE_2_PERSON_OR_FUNDS_PROPERTIES_OVERLAPS_2_VADA = "data/vadalog/use_case_2/people_or_funds_properties_overlaps_2.vada"
USE_CASE_2_PERSON_OR_FUNDS_PROPERTIES_OVERLAPS_1_VADA = "data/vadalog/use_case_2/people_or_funds_properties_overlaps_1.vada"

USE_CASE_3_GET_SHORTEST_PATHS_SOURCES_TARGETS_VADA = "data/vadalog/use_case_3/get_shortest_paths_sources_targets.vada"
USE_CASE_3_EXPLAIN_SHORTEST_PATHS_SOURCES_TARGETS_VADA = "data/vadalog/use_case_3/explain_shortest_paths_sources_targets.vada"
USE_CASE_3_GET_EXPLANATION_SHORTEST_PATHS_SOURCES_TARGETS_VADA = "data/vadalog/use_case_3/get_explanation_shortest_paths_sources_targets.vada"
USE_CASE_3_INDEX_EXPLANATIONS_SHORTEST_PATHS_SOURCES_TARGETS_VADA = "data/vadalog/use_case_3/index_explanations_shortest_paths_sources_targets.vada"
USE_CASE_3_SHORTEST_PATHS_SOURCES_TARGETS_VADA = "data/vadalog/use_case_3/shortest_paths_sources_targets.vada"

client = get_client()
logger = get_logger()
EXPLAIN_ANGEL_RECOMMENDATION_PROMPT = fetch_prompt_config(["src/prompts/angel_summary_01.txt", "integration_tests/use_case_1/angel_summary_01.txt"])
EXPLAIN_EXPERT_RECOMMENDATION_PROMPT = fetch_prompt_config(["src/prompts/expert_summary_01.txt", "integration_tests/use_case_1/expert_summary_01.txt"])
EXPLAIN_SHORTEST_PATH_RECOMMENDATION_PROMPT = fetch_prompt_config(["src/prompts/shortest_path_01.txt", "integration_tests/use_case_3/shortest_path_01.txt"])

# Add at the top of the file with other global variables
current_suggestions = {}
current_expert_suggestions = {}
current_paths_suggestions = {}

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


def recommend_angels_for_company(company_name: str) -> str:
    global current_suggestions
    # here we make the call to Prometheux API via the SDKS
    logger.info(f"Recommend angels for company: {company_name}")
    facts = pmtx.perform(USE_CASE_1_ANGEL_GET_OUTPUT_VADA, {"startup": company_name, "degree_of_separation":"3"})

    # Convert Facts to strings and format them
    formatted_facts = []
    current_suggestions.clear()
    
    for fact in facts[:20]:
        fact_str = str(fact)
        # Updated regex to capture all components
        if match := re.search(r'startup_angel_suggestion\([^|]+\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\)', fact_str):
            angel_name, angel_type, score, degree = match.groups()
            formatted_fact = f"{angel_name} is a {angel_type} angel, with a score of {score} and with a degree of separation of {degree}"
            formatted_facts.append(formatted_fact)
            current_suggestions[angel_name] = fact_str
    
    return "\n".join(formatted_facts)

def recommend_experts_for_company(company_name: str) -> str:
    global current_expert_suggestions
    # here we make the call to Prometheux API via the SDKS
    logger.info(f"Recommend experts for company: {company_name}")
    facts = pmtx.perform(USE_CASE_1_EXPERT_GET_OUTPUT_SUGGESTION_VADA, {"startup": company_name, "degree_of_separation":"3"})

    # Convert Facts to strings and format them
    formatted_facts = []
    current_expert_suggestions.clear()
    
    for fact in facts[:20]:
        fact_str = str(fact)
        # Updated regex to capture all components
        if match := re.search(r'startup_expert_suggestion\([^|]+\|([^|]+)\|([^|]+)\|([^|]+)\)', fact_str):
            expert_name, score, degree = match.groups()
            formatted_fact = f"{expert_name} is an expert, with a score of {score} and with a degree of separation of {degree}"
            formatted_facts.append(formatted_fact)
            current_expert_suggestions[expert_name] = fact_str
    
    return "\n".join(formatted_facts)

def explain_recommend_angel(user_explanation_choice: str) -> str:
    # here we make a call to a chat completion endpoint to summarize Prometheux output
    logger.info(f"Fetching explanation for {user_explanation_choice}")

    full_explanation_key = current_suggestions[user_explanation_choice]
    # explanation = pmtx.perform(USE_CASE_1_ANGEL_GET_EXPLANATION_VADA, {"fact_to_explain": full_explanation_key})
    explanation = pmtx.perform(USE_CASE_1_ANGEL_GET_EXPLANATION_VADA, {"fact_to_explain": full_explanation_key})
    
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

def explain_recommend_expert(expert_explanation_choice: str) -> str:
    # here we make a call to a chat completion endpoint to summarize Prometheux output
    logger.info(f"Fetching explanation for {expert_explanation_choice}")

    full_explanation_key = current_expert_suggestions[expert_explanation_choice]
    logger.info(f"Full explanation key: {full_explanation_key}")
    explanation = pmtx.perform(USE_CASE_1_EXPERT_GET_EXPLANATION_SUGGESTION_VADA, {"fact_to_explain": full_explanation_key})
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": EXPLAIN_EXPERT_RECOMMENDATION_PROMPT},
            {"role": "user", "content": explanation[0].get_arg_by_pos(1)}],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    logger.info(f"Summarized explanation response: {response}")
    
    return response.choices[0].message.content    

def organise_event(number_of_people: int, groups_split: Dict[str, int], topics: List[str], location: str) -> str:
   topics_str = ",".join(topics)
   logger.info(f"Organising event with {number_of_people} people, {groups_split}, {topics_str}, {location}")
   tasks_to_perform = [USE_CASE_2_PERSON_OR_FUNDS_PROPERTIES_OVERLAPS_1_VADA, USE_CASE_2_PERSON_OR_FUNDS_PROPERTIES_OVERLAPS_2_VADA, USE_CASE_2_EXPLAIN_PEOPLE_OR_FUNDS_PROPERTIES_OVERLAPS, USE_CASE_2_INDEX_EXPLANATIONS_PEOPLE_OR_FUNDS_PROPERTIES_OVERLAPS_VADA]

   pmtx.perform(tasks_to_perform, {"requested_properties": f"{location},{topics_str}"})
   logger.info(f"Event organised")

   return "Event organised"
      
def get_shortest_path_sources_targets(source: str, target: str) -> str:
    # used to compute the shortest path between a source and a target
    logger.info(f"Getting shortest path sources targets for {source} and {target}")
    tasks_to_perform = [USE_CASE_3_SHORTEST_PATHS_SOURCES_TARGETS_VADA, \
                       USE_CASE_3_EXPLAIN_SHORTEST_PATHS_SOURCES_TARGETS_VADA, \
                       USE_CASE_3_INDEX_EXPLANATIONS_SHORTEST_PATHS_SOURCES_TARGETS_VADA]
    pmtx.perform(tasks_to_perform, {"source": source, "target": target})
    logger.info(f"Shortest path sources targets computed")

    logger.info(f"Retrieving shortest path sources targets")
    facts = pmtx.perform(USE_CASE_3_GET_SHORTEST_PATHS_SOURCES_TARGETS_VADA)
    extracted_fact = str(facts[0])
    logger.info(f"The shortest path between {source} and {target} is of length {extracted_fact.split("|")[-1]}")

    logger.info(f"Preparing explanation for shortest path sources targets")
    explanation = pmtx.perform(USE_CASE_3_GET_EXPLANATION_SHORTEST_PATHS_SOURCES_TARGETS_VADA, {"fact_to_explain": extracted_fact})
    logger.info(f"raw explanation: {explanation[0].get_arg_by_pos(2)}")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": EXPLAIN_SHORTEST_PATH_RECOMMENDATION_PROMPT},
            {"role": "user", "content": explanation[0].get_arg_by_pos(2)[:2500]}],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    logger.info(f"Summarized explanation response: {response}")
    
    return response.choices[0].message.content    


def display_network_graph():
   pass


def load_tools_from_json(file_path: str) -> List[Dict]:
    with open(file_path, 'r') as file:
        return json.load(file)

tools = load_tools_from_json('tools/tools_config.json')

