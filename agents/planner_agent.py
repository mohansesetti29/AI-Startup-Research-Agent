
from .base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("PlannerAgent")

    def plan(self, query: str):
        self.log(f"Creating research plan for query: {query}")

        base = query.lower()

        tasks = []
        tasks.append(f"competitors for {base}")
        tasks.append(f"market size of {base}")
        tasks.append(f"pain points related to {base}")
        tasks.append(f"opportunities and gaps for {base}")
        tasks.append(f"pricing info for {base}")

        return {"query": query, "tasks": tasks}
