import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader


os.environ.get("HUGGINGFACEHUB_API_TOKEN")
os.environ.get("OPENAI_API_KEY")


def get_website_data(url):
	return 'hi from bot'
    # retriever_chain = get_context_retriever_chain(st.session_state.vector_store)
    # conversation_rag_chain = get_conversational_rag_chain(retriever_chain)

    # response = conversation_rag_chain.invoke({
    #     "chat_history": st.session_state.chat_history,
    #     "input": user_input
    # })
    #return response['answer']

#Function to split data into smaller chunks
# def split_data(docs):
#     text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 1000,
#     chunk_overlap  = 200,
#     length_function = len,
#     )
#     docs_chunks = text_splitter.split_documents(docs)
#     # print(docs_chunks)
#     return docs_chunks

#Function to create embeddings instance
# def create_embeddings():
#     embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
#     return embeddings

# Function to push data to Chroma
# def push_to_chroma(embeddings, chunk_data):
#     Chroma.from_documents(chunk_data, embeddings, persist_directory="./chroma_db")

# Function to pull data from chroma
# def pull_from_chroma(query):
#     db = Chroma(persist_directory="./chroma_db", embedding_function= create_embeddings())
#     docs = db.similarity_search(query)
#     return docs


# Helps us get the summary of a document

# def get_summary(current_doc):
#     llm = OpenAI(temperature=0)
#     #llm = HuggingFaceHub(repo_id="bigscience/bloom", model_kwargs={"temperature":1e-10})
#     chain = load_summarize_chain(llm, chain_type="map_reduce")
#     summary = chain.run([current_doc])
#     return summary