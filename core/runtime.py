from aurion.core.event_bus import EventBus
from aurion.core.scheduler import Scheduler
from aurion.core.state_graph import StateGraph
from aurion.core.sensor_fusion import SensorFusion
from aurion.core.logger import Logger
import random

def run_system():
    logger = Logger()
    bus = EventBus(logger)
    scheduler = Scheduler()
    fusion = SensorFusion()
    graph = StateGraph(logger)

    sensor_buffer = []

    graph.add_transition("IDLE", lambda x: x["value"] > 50, "ACTIVE")
    graph.add_transition("ACTIVE", lambda x: x["value"] < 30, "IDLE")

    def on_sensor(data):
        sensor_buffer.append(data)
        buffer = sensor_buffer[-10:]

        fused = fusion.fuse(buffer)

        print("[FUSED]", fused)

        graph.update(data)
        print("[STATE]", graph.get_state())

    bus.subscribe("sensor", on_sensor)

    def generate_sensor():
        data = {
            "value": random.randint(10, 100),
            "noise": random.uniform(0, 5)
        }
        bus.emit("sensor", data)

    scheduler.add_task(1, generate_sensor)

    print("AURION RUNTIME STARTED")
    scheduler.run()
