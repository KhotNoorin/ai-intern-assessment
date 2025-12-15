import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    default_headers={
        "HTTP-Referer": "https://github.com/KhotNoorin/ai-intern-assessment",
        "X-Title": "AI Intern Assessment"
    }
)

MODEL_NAME = "mistralai/mistral-7b-instruct"


def call_llm(prompt: str, temperature: float = 0.3) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()
