# src/train.py
import os
import mlflow
import mlflow.sklearn
import joblib
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns

MLFLOW_EXPERIMENT_NAME = "iris-classifier"
ARTIFACTS_DIR = "artifacts"
MODEL_PATH = os.path.join(ARTIFACTS_DIR, "model.pkl")
CONF_MATRIX_PATH = "confusion_matrix.png"


def train():
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)

    # 1. Load data
    data = load_iris()
    X = data.data
    y = data.target

    # 2. Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Model
    model = LogisticRegression(max_iter=200)

    # 4. MLflow setup
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)

    with mlflow.start_run():
        # Train
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        # Confusion matrix plot
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(4, 4))
        sns.heatmap(cm, annot=True, fmt="d", cbar=False)
        plt.xlabel("Predicted")
        plt.ylabel("True")
        plt.tight_layout()
        plt.savefig(CONF_MATRIX_PATH)
        plt.close()

        # Log metrics & artifacts
        mlflow.log_metric("accuracy", acc)
        mlflow.log_artifact(CONF_MATRIX_PATH)
        mlflow.sklearn.log_model(model, artifact_path="model")

        # Save model for API use
        joblib.dump(model, MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}, accuracy = {acc:.4f}")


if __name__ == "__main__":
    train()
