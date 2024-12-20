from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

embedding_function = OpenAIEmbeddings()

docs = [
    Document(
        page_content="鼎泰豐由楊秉彝與妻子賴盆妹於1958年在台北創立，最初是販售食用油的小店。1972年轉型為餐廳，以小籠包聞名。現已成為國際知名的台灣美食品牌，在全球多個國家設有分店。",
        metadata={"source": "restaurant_history.txt"},
    ),
    Document(
        page_content="鼎泰豐的小籠包以18摺聞名，每個摺都代表著精湛的手藝。小籠包皮薄餡多，內有鮮美湯汁，是鼎泰豐最受歡迎的招牌菜品。每天現場手工製作，確保新鮮品質。",
        metadata={"source": "signature_dish.txt"},
    ),
    Document(
        page_content="鼎泰豐菜單豐富多樣，除了招牌小籠包外，還有蝦仁燒賣、雞湯餛飩、菜肉餛飩、排骨煨麵、韭黃蝦仁、蛋炒飯等經典菜色。素食選擇包括素小籠包、素蒸餃和各式蔬菜料理。",
        metadata={"source": "menu_items.txt"},
    ),
    Document(
        page_content="鼎泰豐的價格範圍適中，滿足不同消費需求。小籠包每籠（10個）約180-220元，主菜價格從250元到500元不等。套餐選擇豐富，單人套餐約500-700元，雙人套餐約1000-1500元。",
        metadata={"source": "pricing_info.txt"},
    ),
    Document(
        page_content="鼎泰豐台北101旗艦店營業時間為週一至週五11:00-21:30，週六、日及國定假日10:00-21:30。其他分店可能略有不同，建議顧客查詢官網或致電確認。旺季時可能需要排隊等候。",
        metadata={"source": "operation_hours.txt"},
    ),
    Document(
        page_content="鼎泰豐重視食材品質和衛生標準。所有食材每日新鮮配送，嚴格控管儲存溫度。廚房採用開放式設計，顧客可以直接觀看廚師製作過程，體現透明化的製作流程。",
        metadata={"source": "quality_control.txt"},
    ),
    Document(
        page_content="鼎泰豐的服務以親切周到聞名。工作人員接受嚴格培訓，能夠用多國語言服務國際顧客。餐廳內部裝潢簡約現代，保持整潔舒適的用餐環境。",
        metadata={"source": "service_ambiance.txt"},
    ),
    Document(
        page_content="鼎泰豐曾獲得米其林一星評鑑，是台灣首家進入米其林指南的餐廳。它也多次被國際媒體評為世界最佳餐廳之一，成為台灣美食外交的重要代表。",
        metadata={"source": "awards_recognition.txt"},
    ),
    Document(
        page_content="鼎泰豐除了堂食，也提供外帶服務。部分分店與外送平台合作，提供送餐到府服務。公司也有自營的線上商店，販售冷凍小籠包等產品，讓顧客在家也能享受鼎泰豐美味。",
        metadata={"source": "services_products.txt"},
    ),
    Document(
        page_content="鼎泰豐重視永續經營，積極採取環保措施。使用可回收包裝材料，推廣減塑行動。同時也參與社會公益，定期舉辦愛心餐會，回饋社會。",
        metadata={"source": "sustainability_csr.txt"},
    ),
]

db = Chroma.from_documents(docs, embedding_function)
retriever = db.as_retriever()

def retrieve(state):
    print("--- RETRIEVE ---")
    question = state["question"]
    # Retrieval
    documents = retriever.get_relevant_documents(question)
    return {"documents": documents, "question": question}