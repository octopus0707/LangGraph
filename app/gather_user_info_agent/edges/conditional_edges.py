def decide_to_generate(state):
    print("--- ASSESS GRADED DOCUMENTS ---")
    state["question"]
    web_search = state["web_search"]
    state["documents"]

    if web_search == "Yes":
        print("--- DECISION: Re-WRITE ---")
        return "transform_query"
    else:
        print("--- DECISION: GENERATE ---")
        return "generate"