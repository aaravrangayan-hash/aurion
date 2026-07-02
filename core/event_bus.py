from collections import defaultdict

class EventBus:
    def __init__(self, logger=None):
        self.subscribers = defaultdict(list)
        self.logger = logger

    def subscribe(self, event_type, callback):
        self.subscribers[event_type].append(callback)

    def emit(self, event_type, data):
        if self.logger:
            self.logger.log_event(event_type, data)

        for callback in self.subscribers[event_type]:
            callback(data)
