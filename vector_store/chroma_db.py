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



# def answer_query(state):
#     text = state.get("text")
#     if not text:
#         print("No document loaded yet.")
#         return state
    
#     from vector_store.chroma_db import create_vector_store
#     from chains.QA_chain import get_qa_chain
#     vector_store = create_vector_store(chunks)
#     llm = get_llm()
#     qa_chain = get_qa_chain(vector_store, llm)

#     question = input("Enter your question: ")
#     answer = qa_chain.run(question)
#     print(f"Answer: {answer}")
#     return {**state}