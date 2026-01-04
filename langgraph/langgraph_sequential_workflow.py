from langgraph.graph import StateGraph, END
from typing import TypedDict

class DevState(TypedDict):
    feature_request: str
    code: str
    build: str
    deploy: str

def write_code(state: DevState):
    print("Step1 - Writing Code...")
    feature = state["feature_request"]
    return {
        "code" : f"def feature():  return '{feature} implemented'"
    }  

def build_code(state: DevState):
    print("Step2: Building Code...")
    return {
        "build": f"Build successful for -> {state['code']}"
    }

def deploy_code(state: DevState):
    print("Step3: Deploying application...")
    return {
        "deployment" : f"Deployment done using -> {state['build']}"
    }

graph = StateGraph(DevState)

graph.add_node("write_code", write_code)
graph.add_node("build_code", build_code)
graph.add_node("deploy_code", deploy_code)

graph.set_entry_point("write_code")

graph.add_edge("write_code", "build_code")
graph.add_edge("build_code", "deploy_code")
graph.add_edge("deploy_code", END)

app = graph.compile()

result = app.invoke({
    "feature_request" : "Add user login feature"
})

print(result['build'])