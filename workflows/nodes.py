from loaders.pdf_loader import load_pdf
from loaders.ocr_loader import ocr_pdf
from loaders.url_loader import download_pdf
from chains.summarization_chain import get_summary_chain
from chains.QA_chain import build_qa_chain
from vector_store.chroma_db import create_vector_store, delete_vector_store
from utils.text_splitter import split_text
from feedback.feedback_handler import get_feedback
from langchain.schema import Document
import os

def process_document(state):
    action = state.get("action")

    if action == "load_local":
        file_path = state.get("file_path")
        try:
            text = load_pdf(file_path)
        except:
            text = ocr_pdf(file_path)
        # if os.path.exists(file_path):
        #     os.remove(file_path)

        print("Document Loaded Successfully.")
        return {"text": text}

    elif action == "load_url":
        file_url = state.get("file_url")
        file_path = download_pdf(file_url)
        try:
            text = load_pdf(file_path)
        except:
            text = ocr_pdf(file_path)
        if text is None:
            print("Failed to load document from URL.")
        # if os.path.exists(file_path):
        #     os.remove(file_path)
        print("Document Downloaded and Loaded Successfully.")
        return {"text": text}

    elif action == "delete_document":
        delete_vector_store()
        print("Document deleted from vector store.")
        return {"text": ""}

    elif action == "refresh_document":
        text = state.get("text")
        if not text:
            print("No document to refresh.")
            return {}
        chunks = split_text(text)
        create_vector_store(chunks)
        print("🔄 Document refreshed successfully.")
        return {"text": text}

    elif action in ["ask_query"]:
        return {"action": action, "text": state.get("text", "")}

    return {}

def summarize_text(state):
    text = state.get("text")
    docs = [Document(page_content=text)]
    summary_chain = get_summary_chain()
    summary = summary_chain.run(docs)
    return {**state, "summary": summary}

def answer_query(state):
    text = state.get("text")
    if not text:
        print("No document loaded yet.")
        return {}

    chunks = split_text(text)
    vector_store = create_vector_store(chunks)

    qa_chain = build_qa_chain(vector_store.as_retriever())

    query = input("Ask your question: ")
    answer = qa_chain.run(query)

    print(f"\n💬 Answer: {answer}\n")
    return {"answer": answer, "text": text}

def collect_feedback(state):
    feedback = get_feedback()
    return {"feedback": feedback, "text": state.get("text")}
