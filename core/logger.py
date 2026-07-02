import time

class Logger:
    def __init__(self):
        self.logs = []

    def log_event(self, event_type, data):
        self.logs.append({
            "time": time.time(),
            "type": event_type,
            "data": data
        })

    def log_state_change(self, old_state, new_state, reason):
        self.logs.append({
            "time": time.time(),
            "type": "STATE_CHANGE",
            "from": old_state,
            "to": new_state,
            "reason": reason
        })

    def show_logs(self):
        for log in self.logs:
            print(log)

    def replay(self):
        print("\n--- REPLAY START ---")
        for log in self.logs:
            print(log)
            time.sleep(0.2)
        print("--- REPLAY END ---\n")
