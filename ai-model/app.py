from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Model API is running"
    }

@app.get("/predict")
def predict(text: str):
    return {
        "input": text,
        "prediction": f"AI response for: {text}"
    }
