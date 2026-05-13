from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI(title="GenAI Inference API")

# Load artifact on startup
with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

class InferenceRequest(BaseModel):
    prompt: str

@app.post("/predict")
def predict(req: InferenceRequest):
    return {"status": "success", "echo": req.prompt, "vocab_size": len(model["vocab"])}
