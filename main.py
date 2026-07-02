from core.event_bus import EventBus
from core.scheduler import Scheduler
from core.sensor_fusion import SensorFusion
from core.state_graph import StateGraph
from core.logger import Logger
import random

# -------------------------
# INITIALIZE SYSTEM
# -------------------------

logger = Logger()

bus = EventBus(logger)
scheduler = Scheduler()
fusion = SensorFusion()
graph = StateGraph(logger)

sensor_buffer = []

# -------------------------
# STATE MACHINE RULES
# -------------------------

graph.add_transition(
    "IDLE",
    lambda x: x["value"] > 50,
    "ACTIVE"
)

graph.add_transition(
    "ACTIVE",
    lambda x: x["value"] < 30,
    "IDLE"
)

# -------------------------
# SENSOR EVENT HANDLER
# -------------------------

def on_sensor(data):
    sensor_buffer.append(data)

    # keep last 10 readings (sliding window)
    buffer = sensor_buffer[-10:]

    fused = fusion.fuse(buffer)

    print("[FUSED]", fused)

    graph.update(data)

    print("[STATE]", graph.get_state())

# subscribe handler to event bus
bus.subscribe("sensor", on_sensor)

# -------------------------
# SENSOR GENERATOR (SIMULATION)
# -------------------------

def generate_sensor():
    data = {
        "value": random.randint(10, 100),
        "noise": random.uniform(0, 5)
    }

    bus.emit("sensor", data)

# -------------------------
# RUN LOOP (SCHEDULER)
# -------------------------

scheduler.add_task(1, generate_sensor)

print("AURION OBSERVABILITY RUNTIME STARTED")

scheduler.run()
