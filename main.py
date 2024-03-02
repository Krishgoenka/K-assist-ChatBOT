import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


#  environment variables
load_dotenv()

# frontend od streamlit
st.set_page_config(
    page_title="Chat with K-assist chatBOT!",
    page_icon=":brain:",  # cute emoji
    initial_sidebar_state="expanded",
    layout="wide",  
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


st.title("🤖 K-assist ChatBOT")

# chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)


user_prompt = st.chat_input("pucho jo puchna ha ..apun ko sab pata ha")
if user_prompt:
    
    
    st.chat_message("user").markdown(user_prompt)

    # message gemini ko bhejega for result
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # will show result
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
