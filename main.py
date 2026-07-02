from core.event_bus import EventBus
from core.scheduler import Scheduler
from core.sensor_fusion import SensorFusion
from core.state_graph import StateGraph
import random

# system setup
bus = EventBus()
scheduler = Scheduler()
fusion = SensorFusion()
graph = StateGraph()

sensor_buffer = []

# state machine rule
graph.add_transition("IDLE", lambda x: x["value"] > 50, "ACTIVE")

# sensor handler
def on_sensor(data):
    sensor_buffer.append(data)

    # keep last 10 readings
    buffer = sensor_buffer[-10:]

    fused = fusion.fuse(buffer)
    print("[FUSED]", fused)

    graph.update(data)
    print("[STATE]", graph.get_state())

bus.subscribe("sensor", on_sensor)

# fake sensor generator (NO simulator needed)
def generate_sensor():
    data = {
        "value": random.randint(10, 100),
        "noise": random.uniform(0, 5)
    }

    print("[SENSOR]", data)
    bus.emit("sensor", data)

# run every 1 second
scheduler.add_task(1, generate_sensor)

print("AURION SYSTEM STARTED")

scheduler.run()
