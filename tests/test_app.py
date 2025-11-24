"""
Tests for the FastAPI application
"""
import pytest
from fastapi.testclient import TestClient
import joblib
import numpy as np
import os
from pathlib import Path

# Create a dummy model for testing if it doesn't exist
MODEL_PATH = Path("artifacts/model.pkl")
if not MODEL_PATH.exists():
    os.makedirs("artifacts", exist_ok=True)
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    # Train on dummy data
    X = np.array([[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]])
    y = np.array([0, 0, 2])
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    from src.app import app
    return TestClient(app)


def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_endpoint(client):
    """Test the prediction endpoint"""
    # Test with valid iris data
    test_data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], int)
    assert 0 <= response.json()["prediction"] <= 2  # Iris has 3 classes (0, 1, 2)


def test_predict_invalid_data(client):
    """Test prediction endpoint with invalid data"""
    # Test with missing fields
    response = client.post("/predict", json={"sepal_length": 5.1})
    assert response.status_code == 422  # Validation error


def test_predict_negative_values(client):
    """Test prediction with negative values (should still work, but might be invalid)"""
    test_data = {
        "sepal_length": -1.0,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=test_data)
    # Should still return a prediction (model will handle it)
    assert response.status_code == 200

