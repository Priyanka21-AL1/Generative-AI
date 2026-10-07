from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


def chatbot(state: State):
    print("\n\ninside the chatbot node", state)
    return {"messages": ["hii, This is the message from chatbot Node"]}


def samplenode(state: State):
    print("\n\ninside the samplenode node", state)
    return {"messages": ["Sample message appended"]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

updated_state = graph.invoke({
    "messages": ["hi, My name is Priyanka Bangar"]
})

print("\n\nupdated_state", updated_state)

# (START) -> chatbot -> samplenode -> (END)