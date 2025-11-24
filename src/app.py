"""FastAPI application for Iris classification."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path("artifacts/model.pkl")

app = FastAPI(title="Iris Classifier API")

# Load model at startup
model = None
if MODEL_PATH.exists():
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        print(f"Warning: Could not load model: {e}")
else:
    print(f"Warning: Model file not found at {MODEL_PATH}. Run `python -m src.train` first.")


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(input_data: IrisInput):
    """Predict iris class from input features."""
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please train the model first by running `python -m src.train`"
        )
    
    features = np.array(
        [
            [
                input_data.sepal_length,
                input_data.sepal_width,
                input_data.petal_length,
                input_data.petal_width,
            ]
        ]
    )
    try:
        pred = model.predict(features)[0]
        return {"prediction": int(pred)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
