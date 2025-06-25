# Agent A - Streamlit Regulatory Affairs Assistant

This application helps streamline the regulatory affairs workflow for submitting variation applications to the MHRA.

## Setup Instructions

1.  **Create a Python Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2.  **Install Dependencies**
    Install all the required Python libraries using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up Your OpenAI API Key**
    -   Create a new file in this directory named `.env`.
    -   Open the `.env` file and add your OpenAI API key like this:
        ```
        OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ```

## How to Run the App

1.  Make sure you are in the `agent_a_app` directory and your virtual environment is activated.
2.  Run the following command in your terminal:
    ```bash
    streamlit run app.py
    ```
3.  Your web browser will open with the Agent A application running locally.

## Project Structure

