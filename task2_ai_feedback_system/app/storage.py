"""
Storage utilities for Task 2: Two-Dashboard AI Feedback System

This module handles reading from and writing to a shared CSV file
used by both the User and Admin dashboards.
"""

import csv
import os
from datetime import datetime
from typing import Dict, List

# Path to shared data file
DATA_FILE = os.path.join("data", "submissions.csv")


def initialize_storage():
    """
    Ensure the CSV file exists with the correct headers.
    Called once at app startup.
    """
    if not os.path.exists(DATA_FILE):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "user_rating",
                "user_review",
                "ai_response",
                "ai_summary",
                "ai_recommended_action"
            ])


def save_submission(
    user_rating: int,
    user_review: str,
    ai_response: str,
    ai_summary: str,
    ai_recommended_action: str
):
    """
    Append a new submission to the CSV file.
    """
    timestamp = datetime.utcnow().isoformat()

    with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            user_rating,
            user_review,
            ai_response,
            ai_summary,
            ai_recommended_action
        ])


def load_submissions() -> List[Dict]:
    """
    Load all submissions from the CSV file.

    Returns:
        List of dictionaries, each representing a submission.
    """
    submissions = []

    if not os.path.exists(DATA_FILE):
        return submissions

    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            submissions.append(row)

    return submissions