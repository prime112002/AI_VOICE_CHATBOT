import streamlit as st
from utils import get_answer, log_query

import time

# Initialize session state for chat messages
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I assist you today?"}]

initialize_session_state()

st.title("Intelligent Chatbot for Customer Interaction 💬")

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input box
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking 🤔..."):
            try:
                start_time = time.time()
                response = get_answer(st.session_state.messages)
                response_time = time.time() - start_time
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                log_query(user_input, response, response_time)
            except Exception as e:
                st.error(f"Error generating response: {e}")
