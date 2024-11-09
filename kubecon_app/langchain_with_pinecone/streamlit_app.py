# streamlit_app.py
import os
import streamlit as st
import time
from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings
from pinecone import ServerlessSpec
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Pinecone as PineconeVectorStore

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
INDEX_NAME = os.getenv("INDEX_NAME")
NAMESPACE = os.getenv("NAMESPACE")

# Set up Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
cloud = 'aws'
region = "us-east-1"
spec = ServerlessSpec(cloud=cloud, region=region)
index = pc.Index(INDEX_NAME)
time.sleep(1)

# Display the index stats
index_stats = index.describe_index_stats()

# Set up embeddings and vector store
model_name = 'text-embedding-3-small'
embed = OpenAIEmbeddings(model=model_name, openai_api_key=OPENAI_API_KEY)
text_field = "text"

# Vector store
vectorstore = PineconeVectorStore(index, embed.embed_query, text_field, namespace=NAMESPACE)

# Chat model
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo', temperature=0.0)

# Setup the retrieval-based QA system
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# Streamlit UI
st.title("Demo for Langchain and PineCone..")
st.write("Enter your query below:")

query = st.text_input("Query", placeholder="please put your question here ")
if st.button("Get Answer") and query:
    with st.spinner("Fetching answer..."):
        response = qa.invoke(query)
    st.write("### Answer:")
    st.write(response)
