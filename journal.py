import streamlit as st
import datetime
from chat import generate_response
from database import add_journal_entry, get_journal_entries

def journal_page():
    st.title("Daily Journal")
    user = st.text_input("Enter your name", "User")

    journal_entry = st.text_area("Write your thoughts", "Today, I feel...")
    if st.button("Submit Journal"):
        reflection = generate_response(f"User journal entry: {journal_entry}. Provide a reflection.")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_journal_entry(user, journal_entry, reflection, timestamp)
        st.success("Journal saved successfully!")
        st.write(f"AI Reflection: {reflection}")

    st.title("Your Journal Entries")
    entries = get_journal_entries(user)
    for entry in entries:
        st.write(f"Date: {entry[4]}")
        st.write(f"Journal: {entry[2]}")
        st.write(f"Reflection: {entry[3]}")
        st.write("---")
