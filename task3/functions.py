from openai import OpenAI
import json
from problog.program import PrologString
from problog import get_evaluatable

file_path = "variables.json"
with open(file_path, "r") as file:
    data = json.load(file)
openapi_key = data["openapi_key"]


def parse_to_logic(description, info):
    """ Use OpenAI's GPT to convert natural language to Problog logic. """
    ai_client = OpenAI(api_key=openapi_key)

    response = ai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": info},
            {"role": "user", "content": f"Translate this description into Problog logic:\n\n{description}\n\n"}
        ]
    )
    gpt3_response = response.choices[0].message.content
    return gpt3_response


def evaluate_logic(logic_code):
    """ Evaluate the logic code using Problog. """
    model = PrologString(logic_code)
    result = get_evaluatable().create_from(model).evaluate()
    return result
