import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


#  environment variables
load_dotenv()

# frontend of streamlit
st.set_page_config(
    page_title="Chat with K-assist chatBOT!",
    page_icon=":brain:",  # cute emoji
    initial_sidebar_state="expanded",
    layout="wide", 
)


st.title("🤖 K-assist ChatBOT")

st.markdown(
    "K-Assist is a chatbot powered by the Gemini natural language processing model. It generates human-like text, engages in natural conversations, and provides accurate information. With K-Assist, you can"
"Create unique and coherent text on any topic, enhancing your communication and content creation."
"Engage in seamless conversations, overcoming language barriers and improving customer interactions."
"Access a vast knowledge base, retrieving accurate and up-to-date information on a wide range of subjects."
"Customize K-Assist to meet your specific needs, including setting conversation parameters and integrating with other applications."
"Empower your text-based communication and information retrieval with K-Assist today. Unlock the power of AI-driven text generation and conversation, and elevate your interactions to new heights"
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# model setup
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role



if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])




# chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)


user_prompt = st.chat_input("Pucho jo puchna ha /Ask me anything...")
if user_prompt:
    
    
    st.chat_message("user").markdown(user_prompt)

    # message gemini ko bhejega for result
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # will show result
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
