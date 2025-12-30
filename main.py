from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import predict_sales
import uvicorn

app = FastAPI(title="Sales Forecasting API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "OK",
        "message": "Sales Forecasting Backend is running"
    }

from pydantic import BaseModel

class PredictRequest(BaseModel):
    months: int = 6

@app.post("/predict")
def predict(data: dict):
    # Handle both 'months' and 'days' from the frontend
    months = data.get("months", data.get("days", 6))
    return {
        "predictions": predict_sales(months)
    }

# 🔽 ENTRY POINT (PORT 8000)
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
