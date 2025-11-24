"""
Tests for the training script
"""
import pytest
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_imports():
    """Test that all required modules can be imported"""
    import mlflow
    import mlflow.sklearn
    import joblib
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix
    from sklearn.model_selection import train_test_split
    import seaborn as sns
    
    assert mlflow is not None
    assert joblib is not None


def test_train_function():
    """Test that the train function can be imported and called"""
    from src.train import train
    
    # The function should exist and be callable
    assert callable(train)


def test_iris_data_loading():
    """Test that iris dataset can be loaded"""
    from sklearn.datasets import load_iris
    
    data = load_iris()
    assert data is not None
    assert len(data.data) > 0
    assert len(data.target) > 0

