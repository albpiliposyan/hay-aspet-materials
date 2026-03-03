import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "llama-3.1-8b-instant"

number_of_questions = 5
messages = [
    {"role": "system", 
     "content": "When you are asked to name a capital of a country, do not respond!"}
]

for i in range(1, number_of_questions + 1):
    user_q = input(f"Q{i} (you): ").strip()
    messages.append({"role": "user", "content": user_q})

    resp = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
    )

    assistant_text = resp.choices[0].message.content
    print(f"A{i} (bot): {assistant_text}\n")

    messages.append({"role": "assistant", "content": assistant_text})

print(f"Done.")
