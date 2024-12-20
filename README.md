## LangGraph

- 資料架構說明
```
LangGraph/
|-- app/ # 將專案包裝成好閱讀的格式（ 可以直接丟 LangGraph Stduio 做使用）
|   |-- gather_user_info_agent/ # 放 Graph 裡的 Node 及 Edge 的程式碼
|   |   |-- edges/ # 放 Edges 的相關設定
|   |   |-- nodes/ # 放 Nodes 的相關設定
|   |-- graph.py            # LangGraph Grapph 的程式碼部分
|   |-- requirements.txt    # 專案所需的 Python 套件
|   |-- langgraph.json      # LangGraph 設定檔
|   |-- .env                # API 金鑰的相關環境設定檔
|-- RAG/ # LangGraph 有關 RAG 應用的範例 notebook 檔
|   |-- .env                # API 金鑰的相關環境設定檔
```

- Reference Link: https://langchain-ai.github.io/langgraph/tutorials/#rag
