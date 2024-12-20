from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

system = """你是一個問題重寫器，負責將輸入的問題轉換成更適合檢索的優化版本。
分析輸入問題，試圖理解其潛在的語義意圖和含義。
特別注意與鼎泰豐餐廳相關的問題，包括但不限於：
1. 鼎泰豐的歷史和創始人資訊
2. 鼎泰豐的菜單和特色菜品
3. 鼎泰豐的價格範圍
4. 鼎泰豐的營業時間和地點
5. 鼎泰豐的用餐體驗和服務
請根據這些主題來優化問題。"""

re_write_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human","Here is the initial question: \n\n {question} \n Formulate an improved question.")]
)
llm = ChatOpenAI(model="gpt-4o", temperature=0)
question_rewriter = re_write_prompt | llm | StrOutputParser()

def transform_query(state):
    print("--- RE-WRITE QUERY ---")
    question = state["question"]
    documents = state["documents"]

    better_question = question_rewriter.invoke({"question": question})
    return {"documents": documents, "question": better_question}
