"""
LLM interface for Task 2: Two-Dashboard AI Feedback System

This module handles all interactions with the LLM using
a free, open-source model via OpenRouter.
"""

import os
from openai import OpenAI

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Free open-source model
MODEL_NAME = "mistralai/mistral-7b-instruct"


def call_llm(prompt: str, temperature: float = 0.3) -> str:
    """
    Generic LLM call wrapper.

    Args:
        prompt (str): Prompt text
        temperature (float): Controls randomness (lower = more consistent)

    Returns:
        str: LLM-generated text
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()
