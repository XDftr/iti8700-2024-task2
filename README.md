# ChatAI

## Overview

ChatAI is a Python-based application that utilizes the OpenAI API to generate responses to user-defined prompts. 
The application supports responses from two models: GPT-3.5 Turbo and GPT-4. 
This tool is designed to automate the response process for predefined queries and compare model outputs against expected responses.

## Features

- Use of OpenAI's GPT-3.5 Turbo and GPT-4 models to generate text completions.
- Reads predefined prompts and expected answers from a JSON file.
- Saves generated responses to a text file for easy comparison.

## Getting Started

### Prerequisites

- Python 3.x
- openai Python library
- Access to OpenAI's API

### Installation

1. Clone the repository or download the source code:

   ```bash
   git clone https://github.com/XDftr/iti8700-2024-task2
   ```

2. Install the required Python libraries:

   ```bash
   pip install openai
   ```

3. Set up your OpenAI API key:
   
   - Obtain an API key from [OpenAI](https://openai.com).
   - Enter your API key in the `variables.json` file:

     ```json
     {
       "openapi_key": "your-openai-api-key-here"
     }
     ```

### Configuration

- **Data JSON (`data.json`)**: This file should contain an array of objects, each with a `prompt` and `expected_answer` key. The prompts are the queries that will be sent to the AI models, and the expected answers are used to evaluate the responses.

- **Variables JSON (`variables.json`)**: Contains configuration variables such as your OpenAI API key.

### Running the Application

Run the script from the command line:

```bash
python main.py
```

This will process the prompts in `data.json`, use the OpenAI models to generate responses, and save these responses along with the expected answers to `output.txt`.

## Output

Responses are saved to `output.txt`, formatted as follows for each input prompt:

```
Question: [Prompt]
Expected: [Expected Answer]
GPT3.5:   [Response from GPT-3.5]
GPT4:     [Response from GPT-4]

```

## File Structure

- `main.py`: Main Python script containing the logic for reading data, querying OpenAI, and saving responses.
- `data.json`: Input file containing prompts and expected responses.
- `variables.json`: Configuration file containing the OpenAI API key.
- `output.txt`: Output file where the AI responses are saved.

## License

This project is licensed under the Apache License, Version 2.0. See the LICENSE file for more details.

## Possible test dataset
https://allenai.org/data/ruletaker
