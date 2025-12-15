"""
Evaluation utilities for Task 1: Rating Prediction via Prompting

This module provides helper functions to:
- Parse LLM JSON outputs
- Compute accuracy
- Compute JSON validity rate
- Run standardized evaluation loops

Used by:
- task1_prompting_experiments.ipynb
"""

import json
import time
from typing import Callable, Dict

from tqdm import tqdm
import pandas as pd


def parse_llm_response(response: str):
    """
    Safely parse the LLM response as JSON.

    Args:
        response (str): Raw LLM output

    Returns:
        tuple:
            - parsed_json (dict or None)
            - is_valid (bool): whether JSON parsing succeeded
    """
    try:
        parsed = json.loads(response)
        return parsed, True
    except Exception:
        return None, False


def evaluate_prompt(
    prompt_runner: Callable[[str], str],
    df: pd.DataFrame,
    sleep_time: float = 0.4
) -> Dict[str, float]:
    """
    Evaluate a prompt strategy on a dataset.

    Metrics computed:
    - Accuracy (exact star match)
    - JSON validity rate

    Args:
        prompt_runner: Function that takes review text and returns LLM output
        df (pd.DataFrame): DataFrame with columns ['text', 'stars']
        sleep_time (float): Delay between API calls to avoid rate limits

    Returns:
        dict with accuracy and json_validity_rate
    """
    correct = 0
    valid_json = 0
    total = len(df)

    for _, row in tqdm(df.iterrows(), total=total):
        response = prompt_runner(row["text"])
        parsed, is_valid = parse_llm_response(response)

        if is_valid:
            valid_json += 1
            if parsed.get("predicted_stars") == row["stars"]:
                correct += 1

        time.sleep(sleep_time)

    return {
        "accuracy": correct / total,
        "json_validity_rate": valid_json / total
    }


def compare_prompt_strategies(
    prompt_runners: Dict[str, Callable[[str], str]],
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Evaluate and compare multiple prompt strategies.

    Args:
        prompt_runners (dict):
            Mapping of prompt name -> prompt runner function
        df (pd.DataFrame): Evaluation dataset

    Returns:
        pd.DataFrame with metrics for each prompt
    """
    results = []

    for name, runner in prompt_runners.items():
        metrics = evaluate_prompt(runner, df)
        metrics["prompt_version"] = name
        results.append(metrics)

    return pd.DataFrame(results)
