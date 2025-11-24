
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

MODEL_PATH = "artifacts/model.pkl"

app = FastAPI(title="Iris Classifier API")

# Load model at startup
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file not found at {MODEL_PATH}. Run `python -m src.train` first."
    )

model = joblib.load(MODEL_PATH)


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
    pred = model.predict(features)[0]
    return {"prediction": int(pred)}
