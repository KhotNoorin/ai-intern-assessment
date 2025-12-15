"""
User Dashboard (Public-Facing)
Task 2: Two-Dashboard AI Feedback System

Users can:
- Select a star rating
- Write a short review
- Submit feedback
- Receive an AI-generated response

All submissions are stored in a shared CSV file.
"""

import streamlit as st

from app.prompts import user_response_prompt, admin_summary_prompt, admin_action_prompt
from app.llm import call_llm
from app.storage import initialize_storage, save_submission
from app.utils import validate_user_input

# --------------------------------------------------
# App Initialization
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Feedback",
    page_icon="⭐",
    layout="centered"
)

initialize_storage()

st.title("⭐ Customer Feedback")
st.write("We value your feedback! Please share your experience below.")

# --------------------------------------------------
# User Input Section
# --------------------------------------------------
rating = st.selectbox(
    "Select your rating:",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: f"{x} Star{'s' if x > 1 else ''}"
)

review = st.text_area(
    "Write your review:",
    placeholder="Tell us about your experience...",
    height=120
)

submit_btn = st.button("Submit Feedback")

# --------------------------------------------------
# Submission Logic
# --------------------------------------------------
if submit_btn:
    error = validate_user_input(rating, review)

    if error:
        st.error(error)
    else:
        with st.spinner("Generating response..."):
            # Generate AI outputs
            ai_response = call_llm(
                user_response_prompt(rating, review),
                temperature=0.4
            )

            ai_summary = call_llm(
                admin_summary_prompt(rating, review),
                temperature=0.2
            )

            ai_recommended_action = call_llm(
                admin_action_prompt(rating, review),
                temperature=0.3
            )

            # Save submission
            save_submission(
                user_rating=rating,
                user_review=review,
                ai_response=ai_response,
                ai_summary=ai_summary,
                ai_recommended_action=ai_recommended_action
            )

        # Display AI response to user
        st.success("Thank you for your feedback!")
        st.markdown("### 🤖 Our Response")
        st.write(ai_response)