import streamlit as st
import json

# Load FAQ data
with open("admission_faq.json", "r") as f:
    faq_data = json.load(f)

# Search function
def search_answer(query):
    for item in faq_data:
        if query.lower() in item["question"].lower():
            return item["answer"]
    return "Sorry, I couldn't find an answer to your question."

# Streamlit UI
st.title("🎓 College Admission Agent")
st.write("Ask me anything about college admissions!")

user_query = st.text_input("Enter your question below:")

if user_query:
    response = search_answer(user_query)
    st.success(response)
