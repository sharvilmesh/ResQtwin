from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
import random
import time


# ============================================================
# RESQTWIN APPLICATION
# ============================================================

app = FastAPI(
    title="ResQTwin",
    description="Adaptive Digital Twin Rescue Robot",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# FRONTEND PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# ROBOT DIGITAL TWIN
# ============================================================

robot = {
    "id": "RQT-01",

    # Position
    "x": 50.0,
    "y": 50.0,

    # Environmental sensors
    "temperature": 28.0,
    "humidity": 55.0,
    "gas": 120,
    "smoke": 40,

    # Obstacle sensor
    "distance": 100,

    # Robot status
    "status": "ONLINE",

    # Hazard information
    "hazard": False,
    "hazard_type": "NONE"
}


# ============================================================
# SIMULATION SETTINGS
# ============================================================

# Probability of entering a hazard state
HAZARD_PROBABILITY = 0.04

# Number of seconds a simulated hazard lasts
HAZARD_DURATION = 8

hazard_active_until = 0
current_hazard = "NONE"


# ============================================================
# GENERATE NORMAL SENSOR DATA
# ============================================================

def generate_normal_environment():

    robot["temperature"] = round(
        random.uniform(24, 34),
        1
    )

    robot["humidity"] = round(
        random.uniform(40, 70),
        1
    )

    robot["gas"] = random.randint(
        80,
        180
    )

    robot["smoke"] = random.randint(
        20,
        100
    )

    robot["distance"] = random.randint(
        25,
        120
    )


# ============================================================
# GENERATE HAZARDOUS SENSOR DATA
# ============================================================

def generate_hazard_environment(hazard_type):

    if hazard_type == "HIGH TEMPERATURE":

        robot["temperature"] = round(
            random.uniform(42, 55),
            1
        )

        robot["humidity"] = round(
            random.uniform(30, 50),
            1
        )

        robot["gas"] = random.randint(
            80,
            180
        )

        robot["smoke"] = random.randint(
            20,
            100
        )

        robot["distance"] = random.randint(
            30,
            100
        )


    elif hazard_type == "HARMFUL GAS":

        robot["temperature"] = round(
            random.uniform(25, 35),
            1
        )

        robot["humidity"] = round(
            random.uniform(40, 70),
            1
        )

        robot["gas"] = random.randint(
            320,
            500
        )

        robot["smoke"] = random.randint(
            20,
            100
        )

        robot["distance"] = random.randint(
            30,
            100
        )


    elif hazard_type == "SMOKE DETECTED":

        robot["temperature"] = round(
            random.uniform(28, 38),
            1
        )

        robot["humidity"] = round(
            random.uniform(40, 65),
            1
        )

        robot["gas"] = random.randint(
            100,
            200
        )

        robot["smoke"] = random.randint(
            220,
            400
        )

        robot["distance"] = random.randint(
            30,
            100
        )


    elif hazard_type == "OBSTACLE TOO CLOSE":

        robot["temperature"] = round(
            random.uniform(24, 34),
            1
        )

        robot["humidity"] = round(
            random.uniform(40, 70),
            1
        )

        robot["gas"] = random.randint(
            80,
            180
        )

        robot["smoke"] = random.randint(
            20,
            100
        )

        robot["distance"] = random.randint(
            5,
            15
        )


# ============================================================
# HAZARD DETECTION
# ============================================================

def detect_hazard():

    robot["hazard"] = False
    robot["hazard_type"] = "NONE"

    # Temperature hazard
    if robot["temperature"] > 40:

        robot["hazard"] = True
        robot["hazard_type"] = "HIGH TEMPERATURE"


    # Gas hazard
    elif robot["gas"] > 300:

        robot["hazard"] = True
        robot["hazard_type"] = "HARMFUL GAS"


    # Smoke hazard
    elif robot["smoke"] > 200:

        robot["hazard"] = True
        robot["hazard_type"] = "SMOKE DETECTED"


    # Obstacle hazard
    elif robot["distance"] < 20:

        robot["hazard"] = True
        robot["hazard_type"] = "OBSTACLE TOO CLOSE"


# ============================================================
# UPDATE ROBOT SIMULATION
# ============================================================

def update_robot():

    global hazard_active_until
    global current_hazard


    # --------------------------------------------------------
    # ROBOT MOVEMENT
    # --------------------------------------------------------

    robot["x"] += random.uniform(
        -2.0,
        2.0
    )

    robot["y"] += random.uniform(
        -2.0,
        2.0
    )


    # Keep robot inside map

    robot["x"] = max(
        5.0,
        min(95.0, robot["x"])
    )

    robot["y"] = max(
        5.0,
        min(95.0, robot["y"])
    )


    # --------------------------------------------------------
    # HAZARD STATE
    # --------------------------------------------------------

    current_time = time.time()


    # If currently inside a simulated hazard
    if current_time < hazard_active_until:

        generate_hazard_environment(
            current_hazard
        )

    else:

        # Hazard has ended

        current_hazard = "NONE"

        # Randomly create a new hazard

        if random.random() < HAZARD_PROBABILITY:

            current_hazard = random.choice([
                "HIGH TEMPERATURE",
                "HARMFUL GAS",
                "SMOKE DETECTED",
                "OBSTACLE TOO CLOSE"
            ])

            hazard_active_until = (
                current_time +
                HAZARD_DURATION
            )

            generate_hazard_environment(
                current_hazard
            )

        else:

            # Normal environment

            generate_normal_environment()


    # --------------------------------------------------------
    # DETECT HAZARD
    # --------------------------------------------------------

    detect_hazard()


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "project": "ResQTwin",
        "description": "Adaptive Digital Twin Rescue Robot",
        "status": "running"
    }


# ============================================================
# DASHBOARD
# ============================================================

@app.get("/dashboard")
def dashboard():

    return FileResponse(
        BASE_DIR / "frontend" / "index.html"
    )


# ============================================================
# ROBOT TELEMETRY API
# ============================================================

@app.get("/robot")
def get_robot():

    update_robot()

    return {
        "timestamp": time.time(),
        **robot
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "robot": robot["status"]
    }


# ============================================================
# RUN SERVER
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )