from fastapi import FastAPI
from pydantic import BaseModel

class DebugRequest(BaseModel):
    message: str



app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Infra Service is running"}


@app.post("/debug")
def debug(request: DebugRequest):
    return {"received_message": request.message}

#@app.get("/")
#def home():
#    return {"message": "AI Infra Service is running"}

#@app.get("/health")

#def health_check():
#    return {"status": "healthy"}