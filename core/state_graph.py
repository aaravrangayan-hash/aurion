import time

class StateGraph:
    def __init__(self):
        self.state = {}
        self.history = []

    def update(self, key, value):
        self.state[key] = value
        self.history.append((time.time(), key, value))

    def get(self, key, default=None):
        return self.state.get(key, default)

    def snapshot(self):
        return dict(self.state)
