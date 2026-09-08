from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from datetime import datetime
import random
import time

app = FastAPI(
    title="ResQTwin",
    description="Adaptive Digital Twin Rescue Robot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# ROBOT STATE
# ============================================================

robot = {
    "id": "RQT-01",
    "x": 50.0,
    "y": 50.0,
    "temperature": 28.0,
    "humidity": 55.0,
    "gas": 120,
    "smoke": 40,
    "distance": 100,
    "status": "ONLINE",
    "hazard": False,
    "hazard_type": "NONE"
}


# ============================================================
# SIMULATION STATE
# ============================================================

HAZARD_PROBABILITY = 0.04
HAZARD_DURATION = 8

hazard_active_until = 0
current_hazard = "NONE"

# Manual simulation overrides automatic simulation
manual_hazard = None


# ============================================================
# EVENT HISTORY
# ============================================================

event_history = []
last_logged_hazard = "NONE"


def create_event(event_type, status="DETECTED"):

    event = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "type": event_type,
        "status": status,
        "x": round(robot["x"], 1),
        "y": round(robot["y"], 1)
    }

    event_history.insert(0, event)

    # Keep only the latest 20 events
    if len(event_history) > 20:
        event_history.pop()


def log_hazard_change():

    global last_logged_hazard

    current = robot["hazard_type"]

    # New hazard
    if current != "NONE" and current != last_logged_hazard:

        create_event(
            current,
            "DETECTED"
        )

    # Hazard cleared
    elif current == "NONE" and last_logged_hazard != "NONE":

        create_event(
            last_logged_hazard,
            "CLEARED"
        )

    last_logged_hazard = current


# ============================================================
# NORMAL ENVIRONMENT
# ============================================================

def generate_normal_environment():

    robot["temperature"] = round(
        random.uniform(24, 34), 1
    )

    robot["humidity"] = round(
        random.uniform(40, 70), 1
    )

    robot["gas"] = random.randint(
        80, 180
    )

    robot["smoke"] = random.randint(
        20, 100
    )

    robot["distance"] = random.randint(
        25, 120
    )


# ============================================================
# HAZARD ENVIRONMENT
# ============================================================

def generate_hazard_environment(hazard_type):

    if hazard_type == "HIGH TEMPERATURE":

        robot["temperature"] = round(
            random.uniform(45, 58), 1
        )

        robot["humidity"] = random.uniform(
            30, 50
        )

        robot["gas"] = random.randint(
            80, 180
        )

        robot["smoke"] = random.randint(
            250, 450
        )

        robot["distance"] = random.randint(
            30, 100
        )

    elif hazard_type == "HARMFUL GAS":

        robot["temperature"] = round(
            random.uniform(25, 35), 1
        )

        robot["humidity"] = random.uniform(
            40, 70
        )

        robot["gas"] = random.randint(
            420, 650
        )

        robot["smoke"] = random.randint(
            20, 100
        )

        robot["distance"] = random.randint(
            30, 100
        )

    elif hazard_type == "SMOKE DETECTED":

        robot["temperature"] = round(
            random.uniform(30, 38), 1
        )

        robot["humidity"] = random.uniform(
            40, 65
        )

        robot["gas"] = random.randint(
            100, 200
        )

        robot["smoke"] = random.randint(
            450, 650
        )

        robot["distance"] = random.randint(
            30, 100
        )

    elif hazard_type == "OBSTACLE TOO CLOSE":

        robot["temperature"] = round(
            random.uniform(24, 34), 1
        )

        robot["humidity"] = random.uniform(
            40, 70
        )

        robot["gas"] = random.randint(
            80, 180
        )

        robot["smoke"] = random.randint(
            20, 100
        )

        robot["distance"] = random.randint(
            5, 12
        )


# ============================================================
# HAZARD DETECTION
# ============================================================

def detect_hazard():

    robot["hazard"] = False
    robot["hazard_type"] = "NONE"

    if robot["temperature"] > 40:

        robot["hazard"] = True
        robot["hazard_type"] = "HIGH TEMPERATURE"

    elif robot["gas"] > 300:

        robot["hazard"] = True
        robot["hazard_type"] = "HARMFUL GAS"

    elif robot["smoke"] > 200:

        robot["hazard"] = True
        robot["hazard_type"] = "SMOKE DETECTED"

    elif robot["distance"] < 20:

        robot["hazard"] = True
        robot["hazard_type"] = "OBSTACLE TOO CLOSE"


# ============================================================
# ROBOT UPDATE
# ============================================================

def update_robot():

    global hazard_active_until
    global current_hazard

    # Simulated robot movement
    robot["x"] += random.uniform(-2.0, 2.0)
    robot["y"] += random.uniform(-2.0, 2.0)

    robot["x"] = max(
        5.0,
        min(95.0, robot["x"])
    )

    robot["y"] = max(
        5.0,
        min(95.0, robot["y"])
    )


    # --------------------------------------------------------
    # MANUAL SIMULATION
    # --------------------------------------------------------

    if manual_hazard:

        generate_hazard_environment(
            manual_hazard
        )

        detect_hazard()
        log_hazard_change()

        return


    # --------------------------------------------------------
    # AUTOMATIC SIMULATION
    # --------------------------------------------------------

    current_time = time.time()

    if current_time < hazard_active_until:

        generate_hazard_environment(
            current_hazard
        )

    else:

        current_hazard = "NONE"

        if random.random() < HAZARD_PROBABILITY:

            current_hazard = random.choice([
                "HIGH TEMPERATURE",
                "HARMFUL GAS",
                "SMOKE DETECTED",
                "OBSTACLE TOO CLOSE"
            ])

            hazard_active_until = (
                current_time + HAZARD_DURATION
            )

            generate_hazard_environment(
                current_hazard
            )

        else:

            generate_normal_environment()


    detect_hazard()
    log_hazard_change()


# ============================================================
# MANUAL HAZARD SIMULATION
# ============================================================

@app.post("/simulate/{hazard_type}")
def simulate_hazard(hazard_type: str):

    global manual_hazard
    global current_hazard
    global hazard_active_until

    hazard_map = {

        "fire": "HIGH TEMPERATURE",

        "gas": "HARMFUL GAS",

        "smoke": "SMOKE DETECTED",

        "obstacle": "OBSTACLE TOO CLOSE"

    }

    if hazard_type not in hazard_map:

        return {
            "success": False,
            "message": "Unknown hazard type"
        }

    manual_hazard = hazard_map[hazard_type]

    current_hazard = manual_hazard

    hazard_active_until = 0

    generate_hazard_environment(
        manual_hazard
    )

    detect_hazard()

    log_hazard_change()

    return {
        "success": True,
        "hazard": manual_hazard
    }


# ============================================================
# RETURN TO NORMAL
# ============================================================

@app.post("/simulate/normal")
def return_to_normal():

    global manual_hazard
    global current_hazard
    global hazard_active_until

    manual_hazard = None
    current_hazard = "NONE"
    hazard_active_until = 0

    generate_normal_environment()

    detect_hazard()

    log_hazard_change()

    return {
        "success": True,
        "status": "NORMAL"
    }


# ============================================================
# BASIC ROUTES
# ============================================================

@app.get("/")
def home():

    return {
        "project": "ResQTwin",
        "description": "Adaptive Digital Twin Rescue Robot",
        "status": "running"
    }


@app.get("/dashboard")
def dashboard():

    return FileResponse(
        BASE_DIR / "frontend" / "index.html"
    )


@app.get("/robot")
def get_robot():

    update_robot()

    return {
        "timestamp": time.time(),
        **robot
    }


@app.get("/events")
def get_events():

    return {
        "count": len(event_history),
        "events": event_history
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "robot": robot["status"]
    }


# ============================================================
# SERVER
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )