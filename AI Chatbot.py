import streamlit as st
import ollama

st.title("🤖 AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user = st.chat_input("Enter your message")

if user:
    st.session_state.messages.append({"role": "user", "content": user})

    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    ai = response["message"]["content"]

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai
    })

    st.rerun()