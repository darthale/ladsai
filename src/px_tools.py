from typing import List

def recommend_angels_for_company(company_name: str) -> str:
    # here we make the call to Prometheux API via the SDKS
    print(f"Recommend angels for company: {company_name}")
    return "Angel 1 , Angel 2, Angel 3"

def explain_recommend_angel(company_name: str, angel_name: str) -> str:
    # here we make the call to Prometheux API via the SDKS
    print(f"Explain recommendation for angel: {angel_name} for company: {company_name}")
    return "This angel is a good fit for your company because..."

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
}]
