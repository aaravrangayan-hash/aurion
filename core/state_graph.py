class StateGraph:
    def __init__(self, logger=None):
        self.state = "IDLE"
        self.transitions = {}
        self.logger = logger

    def add_transition(self, from_state, condition, to_state):
        self.transitions.setdefault(from_state, []).append((condition, to_state))

    def update(self, input_signal):
        old_state = self.state

        for condition, next_state in self.transitions.get(self.state, []):
            if condition(input_signal):
                self.state = next_state

                if self.logger:
                    self.logger.log_state_change(
                        old_state,
                        self.state,
                        f"Triggered by input: {input_signal}"
                    )
                break

    def get_state(self):
        return self.state
