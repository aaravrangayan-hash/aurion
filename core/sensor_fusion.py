class SensorFusion:
    def __init__(self, state_graph):
        self.state = state_graph

    def process(self, data):
        """
        Converts raw sensor data into meaningful system state
        """

        distance = data.get("distance", 0)
        noise = data.get("noise", 0)

        # simple filtering logic (real systems use Kalman filters)
        filtered_distance = distance - noise * 0.1

        self.state.update("distance", filtered_distance)

        if filtered_distance < 20:
            self.state.update("environment", "DANGER")
        elif filtered_distance < 50:
            self.state.update("environment", "WARNING")
        else:
            self.state.update("environment", "SAFE")

        return self.state.snapshot()
