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
            # scrape website and save to db
            db = push_to_chroma(st.session_state.URL)
            # create retriever chain
            retriever_chain = get_context_retriever_chain(db)
            response = get_website_data(prompt)
            # Append user prompt and response to chat history
            st.session_state.chat_history.append(HumanMessage(content=prompt))
            st.session_state.chat_history.append(AIMessage(content=response))
            retrieved_text = retriever_chain.invoke({
				"chat_history": st.session_state.chat_history,
				"input": "Tell me how"
			})
            with st.sidebar:
                  st.write(retrieved_text)


	    # Display conversation history
        for message in st.session_state.chat_history:
             if isinstance(message, AIMessage):
                  with st.chat_message("AI"):
                        st.write(message.content)
             elif isinstance(message, HumanMessage):
            	 with st.chat_message("Human"):
                	st.write(message.content)
