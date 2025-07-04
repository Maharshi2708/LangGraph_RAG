from langchain.text_splitter import CharacterTextSplitter

def split_text(text):
    text_splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    return text_splitter.create_documents([text])