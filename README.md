<div align="center">

# 🤖 ResQTwin

### Adaptive Digital Twin Rescue Robot for Hazardous Environment Monitoring

*A software-based Digital Twin prototype for simulating a rescue robot operating in hazardous environments.*

</div>

---

## 📖 Overview

**ResQTwin** is a software prototype of an adaptive rescue-robot system designed for hazardous and inaccessible environments.

The project combines a **virtual mobile rescue robot**, simulated environmental sensors, hazard detection, obstacle detection, real-time monitoring, and a **Digital Twin dashboard**.

The system continuously represents the robot's simulated state on a web dashboard, allowing an operator to monitor:

- 📍 Robot position, movement & heading
- 🌡️ Environmental conditions
- 🔥 Detected hazards & hazard location
- 🚨 System alerts
- 🕓 Previous hazard events

> **Note:** The current implementation is a **software simulation/prototype** developed without physical robot hardware.

---

## ✨ Key Features

### 🖥️ Digital Twin Dashboard
A real-time, browser-based dashboard provides a digital representation of the simulated rescue robot — showing robot status, coordinates, heading, sensor readings, hazard status/location, and event history.

### 🧭 Virtual Robot Navigation
The robot moves through a simulated environment while its position is continuously updated on the dashboard, including direction, movement trail, current coordinates, and visual orientation.

### 🌡️ Environmental Monitoring
The prototype simulates key environmental conditions, continuously monitored by the backend:

| Sensor | Purpose |
|---|---|
| 🌡️ Temperature | Detect heat/fire risk |
| 💧 Humidity | Track environmental stability |
| 🧪 Gas Level | Detect gas leaks |
| 💨 Smoke Level | Detect fire/smoke hazards |

### ⚠️ Hazard Detection
Detects simulated hazardous conditions — **Fire, Gas Leak, Smoke, Obstacle** — and generates an alert with the approximate hazard location when triggered.

### 🎛️ Manual Hazard Simulation
Operators can manually trigger emergency scenarios from the dashboard, no physical sensors or robot required:

- 🔥 Simulate Fire
- 🧪 Simulate Gas Leak
- 💨 Simulate Smoke
- 🚧 Simulate Obstacle
- ✅ Return to Normal

### 🕓 Hazard Event History
All detected hazard changes are logged in an event history panel, so operators can review when hazards were detected and when the environment returned to normal.

---

## 🏗️ System Architecture

```
                    ┌──────────────────────────┐
                    │      Web Dashboard        │
                    │                           │
                    │  Robot • Sensors •        │
                    │  Hazards • Alerts •       │
                    │  Event History            │
                    └────────────┬──────────────┘
                                 │
                                 │ HTTP
                                 ▼
                    ┌──────────────────────────┐
                    │      FastAPI Backend      │
                    │                           │
                    │  Robot State              │
                    │  Sensor Simulation        │
                    │  Hazard Detection         │
                    │  Event Logging            │
                    │  Simulation Controls      │
                    └────────────┬──────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Virtual Rescue Robot    │
                    │                           │
                    │  Position                 │
                    │  Movement                 │
                    │  Heading                  │
                    │  Environment              │
                    └──────────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Backend logic and simulation |
| ⚡ FastAPI | REST API |
| 🚀 Uvicorn | Development server |
| 🌐 HTML | Dashboard structure |
| 🎨 CSS | Dashboard interface |
| 📜 JavaScript | Real-time dashboard updates |
| 🔄 JSON | Data exchange |
| 🔧 Git | Version control |
| 🐙 GitHub | Source-code hosting |

---

## 📁 Project Structure

```
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
```

---

## 🔄 Workflow

```
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
```

---

## 🚀 Running the Project

**1. Clone the repository**
```bash
git clone https://github.com/sharvilmesh/ResQtwin.git
```

**2. Enter the project directory**
```bash
cd ResQtwin
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Start the backend**
```bash
python -m src.main
```

**5. Open the dashboard**

Open this address in your browser:
```
http://127.0.0.1:8000/dashboard
```

---

## 🎬 Simulation Scenarios

The dashboard allows different hazardous situations to be demonstrated without physical hardware.

| Scenario | Description |
|---|---|
| 🔥 **Fire** | Simulates a high-temperature hazardous environment |
| 🧪 **Gas Leak** | Simulates elevated gas levels and triggers the corresponding hazard response |
| 💨 **Smoke** | Simulates increased smoke conditions |
| 🚧 **Obstacle** | Simulates an obstacle detected in the robot's environment |
| ✅ **Return to Normal** | Clears the manually simulated hazard and returns the environment to normal operation |

---

## 🌀 Digital Twin Representation

```
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
 │ Digital Twin      │
 │                   │
 │ Position          │
 │ Heading           │
 │ Environment       │
 │ Hazard State      │
 └────────┬──────────┘
          │
          ▼
 ┌──────────────────┐
 │ Operator          │
 │ Dashboard         │
 └──────────────────┘
```

---

## 📌 Current Implementation

**Status:** ✅ Software Prototype / MVP — focused on the simulation layer of the proposed rescue robot.

<details>
<summary><strong>✅ Implemented</strong></summary>

- Virtual robot movement
- Digital Twin dashboard
- Simulated environmental sensors
- Hazard detection
- Hazard alerts
- Hazard location visualization
- Robot heading
- Robot movement trail
- Manual hazard simulation
- Event history
- REST API
- Browser-based monitoring interface

</details>

<details>
<summary><strong>🔮 Future Hardware Integration</strong></summary>

The software architecture can later be extended toward physical hardware such as:

- ESP32
- Raspberry Pi
- Temperature and humidity sensors
- Gas sensors
- Smoke sensors
- Obstacle sensors
- Camera module
- Wireless communication
- Physical mobile robot platform

The current prototype therefore acts as a software foundation for future physical implementation.

</details>

---

## 🗺️ Future Improvements

- [ ] Real-time WebSocket communication
- [ ] Live camera/video simulation
- [ ] Autonomous navigation
- [ ] Obstacle avoidance
- [ ] Mapping
- [ ] Physical sensor integration (ESP32, Raspberry Pi)
- [ ] Remote robot control
- [ ] More advanced Digital Twin visualization
- [ ] Improved hazard localization
- [ ] Autonomous rescue-oriented decision making

---

## 📊 Project Status

> **Current Status:** 🟡 Software Prototype / MVP

ResQTwin currently demonstrates the core software concept of a Digital Twin based rescue-monitoring system through simulation. The project is being developed in stages so that the software architecture can later be connected to physical robotic hardware.

---

## 👤 Author

**Sharvil Meshram**

*Project: ResQTwin — Adaptive Digital Twin Rescue Robot for Hazardous Environment Monitoring*