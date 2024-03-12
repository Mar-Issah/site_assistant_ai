import streamlit as st
from utils import *
# Use the schema below to tell LangChain one is AI and other is human
from langchain_core.messages import AIMessage, HumanMessage
__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

if __name__ == "__main__":
    st.set_page_config(page_title="Website Assistant", page_icon='🤖', layout='centered')

    st.markdown("<h3 style='text-align: center;'>Chat With Website 🤖</h3>", unsafe_allow_html=True)

    # Creating Session State Variable
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = [
            AIMessage(content="Hello, I am a bot. How can I brighten your day?")
        ]
        # w dont want to re-embed the website data every we make a call so lets store it in state
    if 'vector_store' not in st.session_state:
        st.session_state['vector_store'] = ''

    # ********SIDE BAR*******
    with st.sidebar:
        website_url = st.text_input("What's your website URL 🔗", placeholder="https://example.com")

    # Check if URL is empty
    if website_url is None or website_url  == "":
        st.warning("Please enter a website URL!")
    else:
        messages = st.container()
        if prompt := st.chat_input("Say something"):
            # scrape website and save to db
            st.session_state.vector_store = push_to_chroma(website_url)
            # create retriever chain
            response = get_website_data(prompt)
            # Append user prompt and response to chat history
            st.session_state.chat_history.append(HumanMessage(content=prompt))
            st.session_state.chat_history.append(AIMessage(content=response))


	    # Display conversation history
        for message in st.session_state.chat_history:
             if isinstance(message, AIMessage):
                  with st.chat_message("AI"):
                        st.write(message.content)
             elif isinstance(message, HumanMessage):
            	 with st.chat_message("Human"):
                	st.write(message.content)
