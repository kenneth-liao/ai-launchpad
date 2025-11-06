from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Annotated, Literal, List
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, add_messages, END
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langgraph.types import RunnableConfig
from datetime import datetime

load_dotenv()


# Switch models to see how the post quality improves with a more capable model
llm = ChatOpenAI(
    name="ConfigAgent",
    model="gpt-5-mini-2025-08-07",
    reasoning_effort="minimal",
)

class AgentState(BaseModel):
    """The state of the agent."""
    messages: Annotated[list, add_messages] = []

@tool
def get_user_data(config: RunnableConfig):
    """Get the current user's data"""
    return config["configurable"]["user"]


llm_w_tools = llm.bind_tools([get_user_data])

def assistant(state: AgentState):
    system_prompt = SystemMessage(content=f"""You are a helpful assistant. Your job is to help the user with general tasks, questions, and requests.
                                  
    ## Tools
    get_user_data: Use this tool to get the current user's data.
                                  
    Always call the get_user_data tool to get the current user's data. Use the user's data to answer the user's questions.
    """)
    response = llm_w_tools.invoke([system_prompt] + state.messages)
    return {"messages": [response]}

def assistant_router(state: AgentState) -> str:
    if state.messages[-1].tool_calls:
        return "tools"
    return END

builder = StateGraph(AgentState)

builder.add_node(assistant)
builder.add_node("tools", ToolNode([get_user_data]))

builder.set_entry_point("assistant")

builder.add_edge("tools", "assistant")
builder.add_conditional_edges(
    "assistant",
    assistant_router,
    {
        "tools": "tools",
        END: END,
    }
)

graph = builder.compile()

# visualize
from IPython.display import Image
Image(graph.get_graph().draw_mermaid_png())