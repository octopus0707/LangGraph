from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class GradeQuestion(BaseModel):
    """用於檢查問題是否與鼎泰豐餐廳有關"""
    binary_score: str = Field(
        description="問題是否與餐廳有關? 如果是 -> 'yes' 如果不是 -> 'no'"
    )

system = """你是一個評分員,負責評估檢索到的文件與用戶問題的相關性。
只有當問題是關於以下主題時才回答:
1. 鼎泰豐的歷史和創始人資訊
2. 鼎泰豐的菜單和特色菜品
3. 鼎泰豐的價格範圍
4. 鼎泰豐的營業時間和地點
5. 鼎泰豐的用餐體驗和服務

如果問題是關於這些主題,請回答"yes",否則回答"no"。"""

grade_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "user question: {question}")])

llm = ChatOpenAI(model="gpt-4o", temperature=0)
structured_llm = llm.with_structured_output(GradeQuestion)
retrieval_grader = grade_prompt | structured_llm

def grade_documents(state):
    print("--- CHECK DOCUMENT RELEVANCE TO QUESTION ---")
    question = state["question"]
    documents = state["documents"]

    # Score each doc
    filtered_docs = []
    web_search = "No"
    for d in documents:
        score = retrieval_grader.invoke(
            {"question": question, "document": d.page_content}
        )
        grade = score.binary_score
        if grade == "yes":
            print("--- GRADE: DOCUMENT RELEVANT ---")
            filtered_docs.append(d)
        else:
            print("--- GRADE: DOCUMENT NOT RELEVANT ---")
            web_search = "Yes"
            continue
    return {"documents": filtered_docs, "question": question, "web_search": web_search}

