from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from real_model import RealModel

app = FastAPI()

# Load model once
model = RealModel()
model.train()

class StudentData(BaseModel):
    studytime: int
    failures: int
    absences: int
    G1: int
    G2: int

@app.get("/")
def home():
    return {"message": "ML API is running 🚀"}

@app.post("/predict")
def predict(data: StudentData):
    input_data = np.array([[ 
        data.studytime,
        data.failures,
        data.absences,
        data.G1,
        data.G2
    ]])

    prediction = model.model.predict(input_data)[0]

    return {"prediction": float(prediction)}