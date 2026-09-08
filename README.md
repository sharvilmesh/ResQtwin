# ResQTwin
### Adaptive Digital Twin Rescue Robot for Hazardous Environment Monitoring

<p align="center">

**A software-based Digital Twin prototype for simulating a rescue robot operating in hazardous environments.**

</p>

---

## Overview

**ResQTwin** is a software prototype of an adaptive rescue-robot system designed for hazardous and inaccessible environments.

The project combines a **virtual mobile rescue robot**, simulated environmental sensors, hazard detection, obstacle detection, real-time monitoring, and a **Digital Twin dashboard**.

The system continuously represents the robot's simulated state on a web dashboard, allowing an operator to monitor:

- Robot position
- Robot movement
- Robot heading
- Environmental conditions
- Detected hazards
- Hazard location
- System alerts
- Previous hazard events

The current implementation is a **software simulation/prototype** developed without physical robot hardware.

---

## Key Features

### Digital Twin Dashboard

A real-time browser-based dashboard provides a digital representation of the simulated rescue robot.

It displays:

- Robot status
- Robot coordinates
- Robot heading
- Environmental sensor readings
- Hazard status
- Hazard location
- Event history

### Virtual Robot Navigation

The robot moves through a simulated environment while its position is continuously updated on the dashboard.

The dashboard also displays:

- Robot direction
- Movement trail
- Current coordinates
- Visual robot orientation

### Environmental Monitoring

The prototype simulates environmental conditions including:

- Temperature
- Humidity
- Gas level
- Smoke level

These values are continuously monitored by the backend.

### Hazard Detection

The system can detect simulated hazardous conditions such as:

- Fire
- Gas leak
- Smoke
- Obstacle

When a hazardous condition is detected, the system generates an alert and displays the approximate hazard location.

### Manual Hazard Simulation

The dashboard includes controls that allow an operator to manually simulate different emergency scenarios.

Available scenarios:

- Simulate Fire
- Simulate Gas Leak
- Simulate Smoke
- Simulate Obstacle
- Return to Normal

This makes it possible to demonstrate the system without requiring physical sensors or a physical robot.

### Hazard Event History

Detected hazard changes are recorded in an event history panel.

This allows the operator to see when hazards were detected and when the environment returned to normal.

---

## System Architecture

```text
                    ┌──────────────────────────┐
                    │      Web Dashboard       │
                    │                          │
                    │  Robot • Sensors •       │
                    │  Hazards • Alerts •      │
                    │  Event History           │
                    └────────────┬─────────────┘
                                 │
                                 │ HTTP
                                 ▼
                    ┌──────────────────────────┐
                    │      FastAPI Backend      │
                    │                          │
                    │  Robot State             │
                    │  Sensor Simulation       │
                    │  Hazard Detection        │
                    │  Event Logging           │
                    │  Simulation Controls     │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Virtual Rescue Robot   │
                    │                          │
                    │  Position               │
                    │  Movement               │
                    │  Heading                │
                    │  Environment            │
                    └──────────────────────────┘



| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Backend logic and simulation |
| FastAPI    | REST API                     |
| Uvicorn    | Development server           |
| HTML       | Dashboard structure          |
| CSS        | Dashboard interface          |
| JavaScript | Real-time dashboard updates  |
| JSON       | Data exchange                |
| Git        | Version control              |
| GitHub     | Source-code hosting          |



PROJECT STRUCTURE
ResQtwin/
│
├── src/
│   ├── main.py
│   │
│   └── frontend/
│       └── index.html
│
├── requirements.txt
│
└── README.md


WORKFLOW
Start System
     │
     ▼
Initialize Virtual Robot
     │
     ▼
Generate Sensor Data
     │
     ▼
Update Robot Position
     │
     ▼
Check Environmental Conditions
     │
     ▼
Detect Hazard / Obstacle
     │
     ▼
Generate Alert
     │
     ▼
Update Digital Twin
     │
     ▼
Display Information
     │
     ▼
Record Event


RUNNING THE PROJECT
1. Clone the repository
git clone https://github.com/sharvilmesh/ResQtwin.git
2. Enter the project directory
cd ResQtwin
3. Install dependencies
pip install -r requirements.txt
4. Start the backend
python -m src.main
5. Open the dashboard

Open this address in your browser:

http://127.0.0.1:8000/dashboard


SIMULATION SCENARIOS
The dashboard allows different hazardous situations to be demonstrated without physical hardware.

Fire

Simulates a high-temperature hazardous environment.

Gas Leak

Simulates elevated gas levels and triggers the corresponding hazard response.

Smoke

Simulates increased smoke conditions.

Obstacle

Simulates an obstacle detected in the robot's environment.

Return to Normal

Clears the manually simulated hazard and returns the environment to normal operation.

DIGITAL TWIN REPRESENTATION
Physical System Concept
        │
        ▼
 ┌───────────────┐
 │ Rescue Robot  │
 └───────┬───────┘
         │
         │ Sensor / State Data
         ▼
 ┌──────────────────┐
 │ Digital Twin     │
 │                  │
 │ Position         │
 │ Heading          │
 │ Environment      │
 │ Hazard State     │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │ Operator         │
 │ Dashboard        │
 └──────────────────┘


CURRENT IMPLEMENTATION

The current version focuses on the software simulation layer of the proposed rescue robot.

Implemented
Virtual robot movement
Digital Twin dashboard
Simulated environmental sensors
Hazard detection
Hazard alerts
Hazard location visualization
Robot heading
Robot movement trail
Manual hazard simulation
Event history
REST API
Browser-based monitoring interface
Future Hardware Integration

The software architecture can later be extended toward physical hardware such as:

ESP32
Raspberry Pi
Temperature and humidity sensors
Gas sensors
Smoke sensors
Obstacle sensors
Camera module
Wireless communication
Physical mobile robot platform

The current prototype therefore acts as a software foundation for future physical implementation.


FUTURE IMPROVEMENTS

Planned future development may include:

Real-time WebSocket communication
Live camera/video simulation
Autonomous navigation
Obstacle avoidance
Mapping
Physical sensor integration
ESP32 integration
Raspberry Pi integration
Remote robot control
More advanced Digital Twin visualization
Improved hazard localization
Autonomous rescue-oriented decision making



PRJECT STATUS

Current Status: Software Prototype / MVP

ResQTwin currently demonstrates the core software concept of a Digital Twin based rescue-monitoring system through simulation.

The project is being developed in stages so that the software architecture can later be connected to physical robotic hardware.


AUTHOR

Sharvil Meshram

Project: ResQTwin

Adaptive Digital Twin Rescue Robot for Hazardous Environment Monitoring