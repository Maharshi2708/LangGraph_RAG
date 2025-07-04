from langchain.chains.summarize import load_summarize_chain
from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3")

def get_summary_chain():
    return load_summarize_chain(llm, chain_type="stuff")