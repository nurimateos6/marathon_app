import os
import json
from openai import OpenAI


def get_token():
    token_file_path = os.path.join(os.path.dirname(__file__), 'token.json')

    if os.path.exists(token_file_path):
        try:
            with open(token_file_path, 'r') as file:
                credentials = json.load(file)

            token = credentials.get('token')

            if token:
                return token
            else:
                print("Invalid credentials format in the JSON file.")
                return None

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    return None


def chat_with_gpt(user_input: str):
    token = get_token()
    os.environ["OPENAI_API_KEY"] = token

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a fitness coach helping users achieve their health and wellness goals. Provide "
                        "motivation, guidance, and personalized plans for exercise and nutrition."},
            {"role": "user", "content": user_input}
        ]
    )

    return completion.choices[0].message.strip()


if __name__ == '__main__':
    chat_with_gpt('Hi, this is a test')
