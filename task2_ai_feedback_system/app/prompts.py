"""
Prompt templates for Task 2: Two-Dashboard AI Feedback System

This file contains all prompt definitions used for:
- User-facing AI responses
- Admin-facing summaries
- Admin-facing recommended actions

Keeping prompts centralized makes the system easier to
maintain, evaluate, and iterate.
"""


def user_response_prompt(rating: int, review: str) -> str:
    """
    Prompt for generating a polite, empathetic AI response
    shown to the user after submission.
    """
    return f"""
You are an AI assistant for a company receiving customer feedback.

A user has submitted the following feedback:
Rating: {rating} stars
Review: "{review}"

Write a short, polite, and empathetic response to the user.
The response should acknowledge their feedback appropriately
based on the rating.

Do NOT include analysis. Write only the response text.
"""


def admin_summary_prompt(rating: int, review: str) -> str:
    """
    Prompt for generating a concise internal summary
    of the user review for the admin dashboard.
    """
    return f"""
You are an AI assistant helping internal teams analyze customer feedback.

Summarize the following review in 1–2 concise sentences.

Rating: {rating} stars
Review: "{review}"

The summary should be factual and neutral.
Do not add recommendations.
"""


def admin_action_prompt(rating: int, review: str) -> str:
    """
    Prompt for generating recommended next actions
    for internal teams based on user feedback.
    """
    return f"""
You are an AI assistant advising a customer experience team.

Based on the following feedback, suggest 1–2 concrete
recommended actions for the team.

Rating: {rating} stars
Review: "{review}"

Focus on actionable steps such as:
- Follow-up with customer
- Investigate issue
- Maintain current service
- Reward or acknowledge staff

Write clearly and concisely.
"""
