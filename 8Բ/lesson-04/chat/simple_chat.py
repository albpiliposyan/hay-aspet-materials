import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.3-70b-versatile"
# MODEL = "llama-3.1-8b-instant"

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user", 
            "content": "What is the capital of France?"
        },
        {
            "role": "system",
            "content": "Answer in a single word."
        }
    ]
)

print(response.choices[0].message.content)
