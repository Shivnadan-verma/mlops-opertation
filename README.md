# MLflow Learning Project

A machine learning project using MLflow for experiment tracking and FastAPI for model serving.

## Features

- 🧪 MLflow experiment tracking
- 🚀 FastAPI REST API for model predictions
- 🐳 Docker containerization
- 🔄 CI/CD with GitHub Actions
- 📊 Model training and evaluation

## Project Structure

```
mlflow-learning/
├── src/
│   ├── app.py          # FastAPI application
│   └── train.py        # Model training script
├── tests/              # Test files
├── artifacts/          # Trained models
├── mlruns/            # MLflow experiment runs
├── Dockerfile         # Docker configuration
├── requirements.txt   # Python dependencies
└── .github/
    └── workflows/
        └── ci-cd.yml  # GitHub Actions CI/CD pipeline
```

## Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd mlflow-learning
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**
   ```bash
   python -m src.train
   ```

5. **Run the API**
   ```bash
   uvicorn src.app:app --reload
   ```

6. **Test the API**
   ```bash
   # Health check
   curl http://localhost:8000/health
   
   # Make prediction
   curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
   ```

## Docker

### Build Docker Image

```bash
docker build -t mlflow-learning:latest .
```

### Run Docker Container

```bash
docker run -p 8000:8000 mlflow-learning:latest
```

## CI/CD

This project uses GitHub Actions for CI/CD. The pipeline includes:

1. **Testing**: Runs pytest with coverage
2. **Linting**: Code quality checks with flake8 and black
3. **Docker Build**: Builds and pushes Docker images to GitHub Container Registry
4. **Security Scanning**: Vulnerability scanning with Trivy

### GitHub Actions Workflow

The CI/CD pipeline is defined in `.github/workflows/ci-cd.yml` and runs on:
- Push to `main`, `master`, or `develop` branches
- Pull requests to these branches

### Container Registry

Docker images are automatically pushed to GitHub Container Registry:
- `ghcr.io/<your-username>/mlflow-learning:latest`
- `ghcr.io/<your-username>/mlflow-learning:<branch-name>`
- `ghcr.io/<your-username>/mlflow-learning:<commit-sha>`

## Testing

Run tests with pytest:

```bash
pytest tests/ -v
```

Run tests with coverage:

```bash
pytest tests/ -v --cov=src --cov-report=html
```

## API Endpoints

### Health Check
```
GET /health
```

### Prediction
```
POST /predict
Content-Type: application/json

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

## Requirements

- Python 3.10+
- Docker (optional, for containerization)

## License

[Add your license here]
