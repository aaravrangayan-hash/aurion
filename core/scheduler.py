import time

class Scheduler:
    def __init__(self, state_graph):
        self.state = state_graph

    def decide(self):
        env = self.state.get("environment", "SAFE")
        distance = self.state.get("distance", 100)

        if env == "DANGER":
            return {"action": "STOP", "delay": 0}
        elif env == "WARNING":
            return {"action": "SLOW_DOWN", "delay": 0.2}
        else:
            return {"action": "MOVE_FORWARD", "delay": 0.1}

    def execute(self, action_packet):
        time.sleep(action_packet["delay"])
        print(f"[SCHEDULER] ACTION -> {action_packet['action']}")
