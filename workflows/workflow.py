from langgraph.graph import END, StateGraph
from workflows.nodes import process_document, summarize_text, answer_query, collect_feedback

def build_workflow():
    workflow = StateGraph(state_schema=dict)

    workflow.add_node("process_document", process_document)
    workflow.add_node("summarize_text", summarize_text)
    workflow.add_node("answer_query", answer_query)
    workflow.add_node("collect_feedback", collect_feedback)

    workflow.set_entry_point("process_document")

    workflow.add_conditional_edges(
        "process_document",
        lambda state: "summarize_text" if state.get("action") in ["load_local", "load_url"]
        else "answer_query" if state.get("action") == "ask_query"
        else END
    )

    workflow.add_edge("summarize_text", END)
    workflow.add_edge("answer_query", "collect_feedback")
    workflow.add_edge("collect_feedback", END)

    return workflow.compile()
