from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class GradeDocuments(BaseModel):
    """用於檢查檢索到的文檔是否相關。"""

    score: str = Field(
        description="文檔是否與問題相關，'是' 或 '否'"
    )

# 定義 LLM 呼叫流程
system = """你是一個評分員，負責評估檢索到的文檔與用戶問題的相關性。
如果文檔包含與問題相關的關鍵詞或語義含義，請將其評為相關。
給出評分 '是' 或 '否' 來表示文檔是否與問題相關。"""

grade_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "Retrieved document: \n\n {document} \n\n User question: {question}")])

llm = ChatOpenAI(model="gpt-4o", temperature=0)
structured_llm = llm.with_structured_output(GradeDocuments)
docs_grader_llm = grade_prompt | structured_llm
