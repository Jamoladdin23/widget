import os
import numpy as np
import pandas as pd
import requests
import openai
import json

def perform_task(input_value):
    if not input_value.strip():
        return "Error: Empty text entered!"

    # # main processing logic
    result = f"Your data has been processed! You entered: {input_value}\n"
    result += f"Length of your input: {len(input_value)} symbols\n"
    result += f"Text in reverse order: {input_value[::-1]}\n"

    # Additional processing: word count
    word_count = len(input_value.split())
    result += f"Word count: {word_count}\n"

    # Additional processing: converting text to uppercase
    result += f"Text in uppercase: {input_value.upper()}\n"

    return result

# Работа с числовыми данными
def analyze_numbers(input_value):
    try:
        numbers = np.array([float(x) for x in input_value.split(',')])
        mean = numbers.mean()
        median = np.median(numbers)
        return f"Mean: {mean}\nMedian: {median}\n"
    except ValueError:
        return "Error: Please enter a valid list of numbers separated by commas."


# Работа с таблицами (CSV)
def analyze_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        summary = df.describe()  # Описание данных
        output_path = 'output/summary.txt'
        with open(output_path, 'w') as f:
            f.write(summary.to_string())
        return "CSV analysis completed successfully!"
    except Exception as e:
        return f"Error processing CSV file: {e}"


def generate_text(prompt):
    try:
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=100
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error generating text: {e}"


def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            output_path = 'output/api_data.json'
            with open(output_path, 'w') as f:
                json.dump(data, f, indent=4)
            return "API data fetched successfully!"
        else:
            return f"Error: Received status code {response.status_code}"
    except Exception as e:
        return f"Error fetching data: {e}"


def main():
    input_value = os.environ.get('input_value', 'default_value')
    task_type = os.environ.get('task_type', 'text')  # Selecting a task type

    if input_value == 'default_value':
        result = "Error: No input data provided!"
    else:
        if task_type == 'text':
            result = perform_task(input_value)
        elif task_type == 'numbers':
            result = analyze_numbers(input_value)
        elif task_type == 'csv':
            result = analyze_csv('data.csv')  # The file is supposed to be downloaded
        elif task_type == 'ai':
            result = generate_text(input_value)
        elif task_type == 'api':
            result = fetch_data(input_value)
        else:
            result = "Error: Invalid task type!"

    # Save the result in output/result.txt
    output_path = 'output/result.txt'
    os.makedirs('output', exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(result)
    print(f"The result is saved in {output_path}.")


if __name__ == "__main__":
    main()

