import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import  ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


os.environ.get("HUGGINGFACEHUB_API_TOKEN")
os.environ.get("OPENAI_API_KEY")

# we will pass the entire convo, the retrieved chunks and the user prompt and tell the llm that based on the the chat history and the chunks retreived complete the users query


def push_to_chroma(url):
   # get the text in document form
    loader = WebBaseLoader(url)
    document = loader.load()

    # split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # create a vectorstore from the chunks
    db = Chroma.from_documents(document_chunks, SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2"))
    return db

# MessagesPlaceholder is going to hold all the chat history as and when the chat is ongoing otherwsire it is an empty array.
# creates a new retriever that fetches the chunk of text relevant to the chat history and user prompt
def get_context_retriever_chain(vector_store):
    llm = ChatOpenAI()

    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_messages([
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
      ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
    ])
	# creating another retriever object based o history and prompt
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    return retriever_chain

def get_conversational_rag_chain(retriever_chain):

    llm = ChatOpenAI()

    prompt = ChatPromptTemplate.from_messages([
      ("system", "Answer the user's questions based on the below context:\n\n{context}"),
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
    ])

    stuff_documents_chain = create_stuff_documents_chain(llm,prompt)

    return create_retrieval_chain(retriever_chain, stuff_documents_chain)

def get_website_data(url):
    return 'hi'
    # retriever_chain = get_context_retriever_chain(st.session_state.vector_store)
    # conversation_rag_chain = get_conversational_rag_chain(retriever_chain)

    # response = conversation_rag_chain.invoke({
    #     "chat_history": st.session_state.chat_history,
    #     "input": user_input
    # })
    # return response['answer']

