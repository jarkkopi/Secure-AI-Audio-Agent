from typing import TypedDict

class AgentState(TypedDict):
    transcript: str
    security_status: str
    output: str