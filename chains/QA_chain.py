from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama

def get_qa_chain(vector_store, llm):
    qa_prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are an expert AI assistant. Provide a detailed and accurate answer based strictly on the provided context only. Do not add additional information or make assumptions beyond the context or from your knowledge. Kindly stick to the context provided.If the answer is not available in the context, respond with: "The answer is not available in the provided context.
        
        Context: {context}
        Question: {question}
        Answer:
        """)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever = vector_store.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": qa_prompt}
    )

    return qa_chain