
class BaseAgent:
    def __init__(self, name):
        self.name = name

    def log(self, msg):
        print(f"[{self.name}] {msg}")
