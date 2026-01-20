from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("nba_player_points_model.pkl")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlayerInput(BaseModel):
    base_min: float
    base_age: int
    base_gp: int

@app.post("/predict")
def predict_points(data: PlayerInput):
    input_data = np.array([
        data.base_min,
        data.base_age,
        data.base_gp
    ]).reshape(1, -1)

    prediction = model.predict(input_data)[0]

    return {
        "predicted_points": float(prediction)
    }

# Run:
# uvicorn main:app --reload
