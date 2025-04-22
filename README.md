# Data Processing and API Integration Widget

## **Description**
This Python project provides a versatile widget for various tasks, including:
- Text processing.
- Numerical computations.
- CSV file analysis.
- API requests.
- Text generation via OpenAI.

---

## **Features**
1. **Text Processing**:
   - Count characters and words.
   - Reverse text (flip the string).
   - Convert text to uppercase.
2. **Numerical Analysis**:
   - Calculate mean and median from a list of numbers.
3. **CSV File Handling**:
   - Perform descriptive statistics using Pandas.
4. **API Requests**:
   - Fetch JSON data from a provided URL.
5. **AI Text Generation**:
   - Generate text based on user-provided prompts using OpenAI's API.

## **Setup**


## Step 1: Install Python
Ensure Python 3.10 or higher is installed. Verify your version:

bash

    python --version
---

## Create and activate a virtual environment:

    python3 -m venv .venv
    
    source .venv/bin/activate  # MacOS/Linux
    
    .venv\Scripts\activate     # Windows



## Install Dependencies

    pip install -r requirements.txt

## Usage

Input Parameters
Set the following environment variables to configure the widget:
input_value: Input value (text, numbers, URL, or prompt, depending on the task type).
task_type: Type of task—choose from text, numbers, csv, api, or ai.
Run Tasks


## 1.Text Processing:

    export input_value="Hello World!"
    
    export task_type="text"
    
    python run.py

---    


## 2.Numerical Analysis:

    export input_value="1,2,3,4,5"
    
    export task_type="numbers"
    
    python run.py

---

## 3.CSV File Analysis: Ensure the data.csv file exists in the project directory:

    export task_type="csv"
    
    python run.py

---

## 4.AI Text Generation: Ensure your OpenAI API key is set:

    export OPENAI_API_KEY='your_api_key'
    
    export input_value="Generate a story about space exploration."
    
    export task_type="ai"
    
    python run.py

---


## 5.API Requests:

    export input_value="https://jsonplaceholder.typicode.com/posts"
    export task_type="api"
    python run.py

---


## Outputs
Results are saved in the output folder:

output/result.txt: Text, numerical, or AI results.

output/summary.txt: CSV analysis results.

output/api_data.json: API data results.

---

## Editing
If you need to modify the widget:

Update the code in run.py.

Test the updated functionality.

Install any new dependencies via:

    pip install -r requirements.txt

