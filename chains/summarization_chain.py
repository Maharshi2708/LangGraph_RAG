from langchain.chains.summarize import load_summarize_chain
from langchain_ollama import ChatOllama


def get_summary_chain():
    llm = ChatOllama(model="phi3")
    return load_summarize_chain(llm, chain_type="stuff")