from collections import defaultdict
import threading

class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)

    def emit(self, event_type, data=None):
        if event_type not in self.listeners:
            return

        for cb in self.listeners[event_type]:
            # run async so system doesn't freeze
            threading.Thread(target=cb, args=(data,)).start()
