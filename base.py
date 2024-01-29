import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def communicate_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # GPT-4.0 Turbo model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def main():
    print("Welcome to the Diabetes Education Toolkit!")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Exiting the toolkit. Goodbye!")
            break

        # Communicate with GPT for a response
        gpt_response = communicate_with_gpt(user_input)

        print(f"Toolkit: {gpt_response}")

if __name__ == "__main__":
    main()
