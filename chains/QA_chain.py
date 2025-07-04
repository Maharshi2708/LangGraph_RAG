from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama


def build_qa_chain(retriever):
    llm = ChatOllama(model="phi3")
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)