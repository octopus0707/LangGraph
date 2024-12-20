from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o", temperature=0)
template = """Answer the question based only on the following context:{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template=template)
rag_chain = prompt | llm | StrOutputParser()

def generate(state):
    print("--- GENERATE ---")
    question = state["question"]
    documents = state["documents"]

    # RAG generation
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}
