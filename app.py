import streamlit as st
from chat import generate_response
from journal import journal_page
from quotes import get_motivational_quote
from resources import resource_page
from database import init_db

# Initialize the database
init_db()

st.set_page_config(page_title="Mental Health AI Chatbot", layout="wide")

st.sidebar.title("Mental Health Support")
selection = st.sidebar.radio("Choose a feature:", ["Chat", "Journal", "Motivational Quotes", "Resources"])

if selection == "Chat":
    st.title("Chat with the AI")
    user_input = st.text_input("You: ", "How are you feeling today?")
    if user_input:
        bot_response = generate_response(user_input)
        st.write(f"Bot: {bot_response}")
elif selection == "Journal":
    journal_page()
elif selection == "Motivational Quotes":
    st.title("Daily Motivational Quotes")
    st.write(get_motivational_quote())
elif selection == "Resources":
    resource_page()

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap');
    body {font-family: 'Roboto', sans-serif;}
    </style>
    """,
    unsafe_allow_html=True
)

