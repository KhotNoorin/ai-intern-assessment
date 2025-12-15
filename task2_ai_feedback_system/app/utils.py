"""
Utility functions for Task 2: Two-Dashboard AI Feedback System

This module contains helper functions used across
user and admin dashboards.
"""

from typing import Optional


def validate_user_input(rating: int, review: str) -> Optional[str]:
    """
    Validate user input before submission.

    Args:
        rating (int): Star rating selected by user
        review (str): Review text entered by user

    Returns:
        None if valid, otherwise an error message string
    """
    if rating is None or rating < 1 or rating > 5:
        return "Please select a valid star rating (1–5)."

    if not review or len(review.strip()) < 5:
        return "Please write a short review (at least 5 characters)."

    return None


def truncate_text(text: str, max_length: int = 200) -> str:
    """
    Truncate long text for display in dashboards.

    Args:
        text (str): Input text
        max_length (int): Maximum allowed length

    Returns:
        Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
