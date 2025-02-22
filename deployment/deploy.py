from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any
import uvicorn
import joblib
import os
import numpy as np 

app = FastAPI(title="ML Model API")

model = None

class PredictionRequest(BaseModel):
    age: int
    height: float
    weight: float
    waist: float
    eyesight_left: float
    eyesight_right: float
    hearing_left: float
    hearing_right: float
    systolic: int
    relaxation: int
    fasting_blood_sugar: float
    cholesterol: float
    triglyceride: float
    hdl: float
    ldl: float
    hemoglobin: float
    urine_protein: float
    serum_creatinine: float
    ast: float
    alt: float
    gtp: float
    dental_caries: int

class PredictionResponse(BaseModel):
    prediction: Any
    probability: float

@app.on_event("startup")
async def load_model():
    global model
    model_path = "model.bin"
    if os.path.exists(model_path):
        model = joblib.load(model_path)
    else:
        raise HTTPException(status_code=500, detail="Model file not found.")

@app.get("/")
async def root():
    return {"message": "ML Model API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        input_data = np.array([
            [
                request.age,
                request.height,
                request.weight,
                request.waist,
                request.eyesight_left,
                request.eyesight_right,
                request.hearing_left,
                request.hearing_right,
                request.systolic,
                request.relaxation,
                request.fasting_blood_sugar,
                request.cholesterol,
                request.triglyceride,
                request.hdl,
                request.ldl,
                request.hemoglobin,
                request.urine_protein,
                request.serum_creatinine,
                request.ast,
                request.alt,
                request.gtp,
                request.dental_caries
            ]
        ])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data).max()

        return PredictionResponse(prediction=prediction, probability=probability)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
