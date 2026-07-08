from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": "You are an expert in mathematics."
        },
        {
            "role": "user",
            "content": "Can you solve (a-b)^2?"
        }
    ]
)

print(response.choices[0].message.content)