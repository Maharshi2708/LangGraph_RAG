from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    text = " ".join([page.page_content for page in pages])
    if not text or len(text) < 50:
        raise Exception("Loaded Content is empty or too short, possibly a scanned pdf.")
    return text