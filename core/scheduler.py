import time

class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, interval, func):
        self.tasks.append({
            "interval": interval,
            "func": func,
            "last": 0
        })

    def run(self):
        while True:
            now = time.time()

            for task in self.tasks:
                if now - task["last"] >= task["interval"]:
                    task["func"]()
                    task["last"] = now
