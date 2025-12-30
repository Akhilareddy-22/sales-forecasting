# Sales Forecasting Project

## Overview
Predict future sales using time-series ML (ARIMA) with frontend dashboard,
backend API, and Docker deployment.

## Architecture
Dataset → ML Model → Backend API → Frontend Dashboard

## How to Run (Without Docker)

1. Install dependencies
pip install -r requirements.txt

2. Train model
python ml/train_model.py

3. Run backend
uvicorn backend.main:app --reload

4. Open frontend
Open frontend/index.html in browser

## How to Run (With Docker)

docker-compose up --build

Backend runs at:
http://localhost:8000

## API
POST /predict?days=N

## Output
Predicted sales numbers shown in chart and list.

## Note
No manual sales entry.
User only selects forecast duration.
