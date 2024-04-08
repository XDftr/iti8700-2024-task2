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

    def ask_chat(self, message):
        messages = []
        c = "Give short answer only. Maximum 1 sentence. Prefer 1 word."

        messages.append({
            "role": "user",
            "content": c
        })

        messages.append({
            "role": "user",
            "content": message
        })

        chat_response_gpt3 = self.ai_client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )

        chat_response_gpt4 = self.ai_client.chat.completions.create(
            messages=messages,
            model="gpt-4",
        )

        gpt3_response = chat_response_gpt3.choices[0].message.content
        gpt4_response = chat_response_gpt4.choices[0].message.content

        return gpt3_response, gpt4_response

    def read_input_data(self):
        file_path = "data.json"
        with open(file_path, "r") as file:
            self.input_data = json.load(file)

    def read_properties(self):
        file_path = "variables.json"
        with open(file_path, "r") as file:
            data = json.load(file)
        self.openapi_key = data["openapi_key"]

    def ask_questions(self):
        for question in self.input_data:
            gpt3_response, gpt4_response = self.ask_chat(question["prompt"])
            self.output_data.append({
                "question": question["prompt"],
                "gpt3_response": gpt3_response,
                "gpt4_response": gpt4_response,
                "expected_response": question["expected_answer"]
            })

    def save_responses(self):
        file_path = "output.txt"
        with open(file_path, "w") as file:
            for response in self.output_data:
                q = response["question"]
                g3 = response["gpt3_response"]
                g4 = response["gpt4_response"]
                e = response["expected_response"]
                file.write(f"Question: {q}\nExpected: {e}\nGPT3.5:   {g3}\nGPT4:     {g4}\n\n")

    def run(self):
        self.ask_questions()
        self.save_responses()


if __name__ == '__main__':
    chat = ChatAI()
    chat.run()
