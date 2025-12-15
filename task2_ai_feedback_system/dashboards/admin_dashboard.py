"""
Admin Dashboard (Internal-Facing)
Task 2: Two-Dashboard AI Feedback System

Displays:
- All user submissions
- AI-generated summaries
- AI-recommended actions
- Basic analytics
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



import streamlit as st
import pandas as pd

from app.storage import initialize_storage, load_submissions
from app.utils import truncate_text

# --------------------------------------------------
# App Initialization
# --------------------------------------------------
st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="📊",
    layout="wide"
)

initialize_storage()

st.title("📊 Admin Dashboard")
st.write("Internal view of all customer feedback and AI insights.")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
submissions = load_submissions()

if not submissions:
    st.info("No submissions yet.")
    st.stop()

df = pd.DataFrame(submissions)

# --------------------------------------------------
# Basic Analytics
# --------------------------------------------------
st.subheader("📈 Feedback Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Submissions", len(df))

with col2:
    avg_rating = round(df["user_rating"].astype(int).mean(), 2)
    st.metric("Average Rating", avg_rating)

with col3:
    low_ratings = (df["user_rating"].astype(int) <= 2).sum()
    st.metric("Low Ratings (≤2)", low_ratings)

# --------------------------------------------------
# Submissions Table
# --------------------------------------------------
st.subheader("🗂️ All Submissions")

df_display = df.copy()

df_display["user_review"] = df_display["user_review"].apply(
    lambda x: truncate_text(x, 100)
)

df_display["ai_response"] = df_display["ai_response"].apply(
    lambda x: truncate_text(x, 100)
)

df_display["ai_summary"] = df_display["ai_summary"].apply(
    lambda x: truncate_text(x, 100)
)

df_display["ai_recommended_action"] = df_display["ai_recommended_action"].apply(
    lambda x: truncate_text(x, 100)
)

st.dataframe(df_display, use_container_width=True)

# --------------------------------------------------
# Detailed View
# --------------------------------------------------
st.subheader("🔍 Detailed Submission View")

selected_index = st.selectbox(
    "Select a submission to view details:",
    options=df.index,
    format_func=lambda i: f"Submission {i + 1} | Rating: {df.loc[i, 'user_rating']}⭐"
)

selected_row = df.loc[selected_index]

st.markdown("### ⭐ User Rating")
st.write(selected_row["user_rating"])

st.markdown("### 📝 User Review")
st.write(selected_row["user_review"])

st.markdown("### 🤖 AI Response to User")
st.write(selected_row["ai_response"])

st.markdown("### 📌 AI Summary")
st.write(selected_row["ai_summary"])

st.markdown("### ✅ AI Recommended Action")
st.write(selected_row["ai_recommended_action"])