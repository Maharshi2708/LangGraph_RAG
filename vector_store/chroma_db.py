from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
import shutil

DB_DIR = ""
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vector_store(chunks):
    return Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="DB_DIR")

def delete_vector_store():
    if os.path.exists(DB_DIR):
        shutil.rmtree(DB_DIR)