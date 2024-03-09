import streamlit as st
from utils import *
# Use the schema below to tell LangChain one is AI and other is human
from langchain_core.messages import AIMessage, HumanMessage

if __name__ == "__main__":
    st.set_page_config(page_title="Website Assistant", page_icon='🤖', layout='centered')

    st.markdown("<h3 style='text-align: center;'>Chat With Website 🤖</h3>", unsafe_allow_html=True)

    # Creating Session State Variable
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = [
            AIMessage(content="Hello, I am a bot. How can I brighten your day?")
        ]
    if 'URL' not in st.session_state:
        st.session_state['URL'] = ''

    # ********SIDE BAR*******
    with st.sidebar:
        st.session_state['URL'] = st.text_input("What's your website URL 🔗", placeholder="https://example.com")

    # Check if URL is empty
    if st.session_state['URL'] is None or st.session_state['URL'] == "":
        st.warning("Please enter a website URL!")
    else:
        messages = st.container()
        if prompt := st.chat_input("Say something"):
            response = get_website_data(prompt)
            # Append user prompt and response to chat history in order to display conversation history
            st.session_state.chat_history.append(HumanMessage(content=prompt))
            st.session_state.chat_history.append(AIMessage(content=response))
            st.write(st.session_state.chat_history)

	    # Display conversation history