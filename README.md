**Adaptive Unified Robotics & IoT Orchestration Network**

AURION is a distributed control framework for embedded systems that unifies sensors, microcontrollers, and actuators into a single event-driven state graph.

It enables real-time coordination between heterogeneous hardware nodes using a shared event bus, sensor fusion engine, and deterministic actuation scheduler.

---

## Core Concept

Instead of isolated microcontroller logic, AURION treats all devices as nodes in a shared computational graph.

Each node:
- emits events (sensor updates, state changes)
- subscribes to system-wide signals
- executes controlled actuation commands

---

## Architecture


Sensors → Event Bus → State Graph → Decision Engine → Actuators


### Modules

- **Event Bus**: real-time message propagation system
- **State Graph**: global system state representation
- **Sensor Fusion**: merges multi-sensor inputs into unified state
- **Scheduler**: resolves actuator conflicts + timing constraints
- **Telemetry Layer**: logs full system behavior over time

---

## Supported Nodes

- Arduino (serial-based communication)
- ESP32 (WiFi/MQTT-ready extension)
- Raspberry Pi (Python-native node)
- Simulated nodes (for testing logic without hardware)

---

## Example Use Case

A drone system:

- ultrasonic sensor detects obstacle
- IMU detects tilt correction needed
- event bus triggers avoidance logic
- scheduler adjusts motor output in real time

---

## Installation

```bash
git clone https://github.com/yourname/aurion.git
cd aurion
pip install -r requirements.txt
Run Example
python main.py
Status

Early-stage systems prototype:

event system: stable
node abstraction: in progress
hardware integration: experimental
Vision

AURION aims to become a unified control plane for distributed physical computing systems.


---

# core/event_bus.py

```python
class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def emit(self, event_type, data):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)
