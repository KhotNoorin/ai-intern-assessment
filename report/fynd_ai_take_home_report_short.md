# Fynd AI Intern – Take Home Assessment 

**Candidate:** Noorin Nasir Khot  
**Role:** AI Intern  

---

## Overview

This project demonstrates how **Large Language Models (LLMs)** can be used effectively through **prompt engineering and clean system design**, without training any models.

The assessment consists of two parts:
- **Task 1:** Predicting Yelp review ratings (1–5 stars) using prompt-based classification
- **Task 2:** Building and deploying a two-dashboard AI feedback system (User + Admin)

Only **free LLM APIs** were used, as allowed in the instructions.

---

## Tools & LLMs Used

- **LLM Provider:** OpenRouter  
- **Model:** Mistral-7B (open-source, free tier)  
- **Language:** Python  
- **Framework:** Streamlit  
- **Storage:** CSV (shared lightweight store)

The LLM was treated as a **controlled system component**, not a black-box magic solution.

---

## Task 1 – Rating Prediction via Prompting

### Objective
Classify Yelp restaurant reviews into **1–5 star ratings** and return predictions in **strict JSON format**.

### Approach
Three prompt strategies were tested on a sample of **200 reviews**:

1. **Baseline Prompt** – minimal instructions  
2. **Rubric-Based Prompt** – explicit definitions for each rating  
3. **Reasoned + JSON Guard Prompt** – step-by-step reasoning with strict output rules  

### Results (Summary)

| Prompt Version | Accuracy | JSON Validity |
|---------------|----------|---------------|
| Baseline | ~50% | ~85% |
| Rubric-Based | ~60% | ~93% |
| Reasoned + Guard | ~70% | ~98% |

**Key Insight:**  
Adding clear reasoning steps and strict output constraints significantly improved reliability and consistency, without any model training.

---

## Task 2 – Two-Dashboard AI Feedback System

### User Dashboard (Public)
- Users submit a star rating and short review
- AI generates a polite, empathetic response
- Feedback is stored automatically

### Admin Dashboard (Internal)
- View all user submissions
- AI-generated summaries
- AI-recommended actions
- Basic analytics (average rating, low ratings)

Both dashboards read and write from the **same shared data source**, ensuring consistency.

---

## Deployment

Both dashboards were deployed on **Streamlit Cloud** using environment-based API keys.

- **User Dashboard URL:** *(submitted separately)*  
- **Admin Dashboard URL:** *(submitted separately)*  

---

## Design Choices & Learnings

- Prompt engineering can effectively replace model training for many tasks
- Centralizing prompts improves consistency and maintainability
- Lightweight CSV storage is sufficient for low-traffic applications
- Modular design simplifies debugging and deployment

---

## Conclusion

This project shows how **well-designed prompts, evaluation, and deployment** can turn LLMs into reliable, real-world systems.  
The focus was on building something **usable, explainable, and production-ready**, not just generating outputs.
 
