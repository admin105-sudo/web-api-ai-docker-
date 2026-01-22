from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI service running"}

@app.get("/predict")
def predict(value: int = 1):
    return {"input": value, "output": value * 2}
