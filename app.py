import yaml
import json
from mistralai import Mistral

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

api_key = config.get("mistral_api_key", "")
model = config.get("model", "mistral-large-latest")

with open("system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()


def react_agent(user_message: str, functions_table: str = None) -> dict:

    
    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.1,
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)

def analyze_sql_result(sql_result: str) -> dict:
    pass

def analyze_answer_with_sql(question: str, sql_result: str) -> dict:
    pass
