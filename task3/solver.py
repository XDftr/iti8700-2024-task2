import json
from functions import parse_to_logic, evaluate_logic

with open("input_data.json", "r") as file:
    input_data = json.load(file)

with open("initial.txt", "r") as file:
    inp = " ".join(file.readlines())

index = 1

for data in input_data:
    print("Running question:", index)
    file = open(f"responses/response_{index}.txt", "w")
    index += 1

    desc = data['facts'] + " Question: " + data['question']

    file.write("Statements:\n")
    file.write(data['facts'] + "\n\n")

    file.write("Question:\n")
    file.write(data['question'] + "\n\n")

    file.write("GPT response\n")

    logic_output = ""
    try:
        logic_output = parse_to_logic(desc.strip(), inp)
        file.write(logic_output + "\n\n")
    except Exception:
        file.write("Error")

    file.write("Problog response:\n")

    if logic_output:
        try:
            results = evaluate_logic(logic_output)
            file.write(str(results))
        except Exception:
            file.write("Error")
    else:
        file.write("Error")

    file.close()
