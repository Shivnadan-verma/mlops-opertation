# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system deps if needed (optional)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything (src, artifacts, mlruns if you want)
COPY . .

# By default, just start API (assume model is already trained)
EXPOSE 5000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
