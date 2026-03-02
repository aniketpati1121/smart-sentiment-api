from fastapi import FastAPI
from app.model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Sentiment API is running"}

@app.get("/predict")
def get_prediction(text: str):
    result = predict(text)
    sentiment = "Positive" if result == 1 else "Negative"
    return {"sentiment": sentiment} 

#  uvicorn app.main:app --reload