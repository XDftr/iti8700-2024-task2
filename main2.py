# -----------------------------------------------------------------
# Copyright (c) 2024 Deniel Konstantinov
# deniel.konstantinov@outlook.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------

from openai import OpenAI
import json


class ChatAI:
    def __init__(self):
        self.openapi_key = None
        self.read_properties()
        self.ai_client = OpenAI(api_key=self.openapi_key)

        self.input_data = []
        self.read_input_data()

        self.output_data = []

        self.total = 0
        self.gpt3_true = 0
        self.gpt4_true = 0
        self.gpt4_and_3_wrong = 0

    def ask_chat(self, data, message, expected):
        messages = []
        c = "Respond with True or False only."

        messages.append({
            "role": "user",
            "content": c
        })

        messages.append({
            "role": "user",
            "content": data
        })

        messages.append({
            "role": "user",
            "content": f"Statement: {message}"
        })

        chat_response_gpt3 = self.ai_client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )
        gpt3_response = chat_response_gpt3.choices[0].message.content

        if f"{expected}" in gpt3_response:
            self.gpt3_true += 1

        chat_response_gpt4 = self.ai_client.chat.completions.create(
            messages=messages,
            model="gpt-4",
        )
        gpt4_response = chat_response_gpt4.choices[0].message.content

        if f"{expected}" in gpt4_response:
            self.gpt4_true += 1

        if f"{expected}" not in gpt4_response and f"{expected}" not in gpt3_response:
            self.gpt4_and_3_wrong += 1

        self.total += 1

        return gpt3_response, gpt4_response

    def read_input_data(self):
        file_path = "dev.jsonl"
        with open(file_path, "r") as file:
            for line in file.readlines():
                json_object = json.loads(line)
                text = json_object["context"]
                questions = json_object["questions"]
                parsed_questions = []
                for question in questions:
                    parsed_questions.append({
                        "text": question["text"],
                        "value": question["label"]
                    })
                self.input_data.append({
                    "data": text,
                    "questions": parsed_questions
                })

    def read_properties(self):
        file_path = "variables.json"
        with open(file_path, "r") as file:
            data = json.load(file)
        self.openapi_key = data["openapi_key"]

    def ask_questions(self):
        for data in self.input_data[:10]:
            for q in data["questions"]:
                gpt3_response, gpt4_response = self.ask_chat(data["data"], q["text"], q["value"])
                self.output_data.append({
                    "data": data["data"],
                    "question": q["text"],
                    "gpt3_response": gpt3_response,
                    "gpt4_response": gpt4_response,
                    "expected_response": q["value"]
                })

    def save_responses(self):
        file_path = "output2.txt"
        with open(file_path, "w") as file:
            file.write(
                f"Total: {self.total}, GPT3 True: {self.gpt3_true}, GPT4 True: {self.gpt4_true}, Both wrong: {self.gpt4_and_3_wrong}\n\n")
            for response in self.output_data:
                data = response["data"]
                q = response["question"]
                g3 = response["gpt3_response"]
                g4 = response["gpt4_response"]
                e = response["expected_response"]
                file.write(f"Data: {data} \nQuestion: {q}\nExpected: {e}\nGPT3.5:   {g3}\nGPT4:     {g4}\n\n")

    def run(self):
        self.ask_questions()
        self.save_responses()


if __name__ == '__main__':
    chat = ChatAI()
    chat.run()
