import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def call_gpt_for_budget(project_type):
    """
    Call GPT API to generate a budget based on project type.
    :param project_type: The type of project.
    :return: Raw response content from GPT.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"Generate a budget for a '{project_type}' project. Response in json format with root keys as modules, phases, and costs."
            }
        ],
        max_tokens=150
    )

    # Return the raw response content from the GPT model
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    project_type = input("Enter the project type (e.g., 'pos for restaurant'): ").strip().lower()
    response_content = call_gpt_for_budget(project_type)
    print("Response from GPT model:")
    print(response_content)
