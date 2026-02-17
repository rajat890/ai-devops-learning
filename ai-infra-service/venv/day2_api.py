from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DebugRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "AI Infra Service is runningg"}


@app.post("/debug")
def debug(request: DebugRequest):
    user_message = request.message.lower()

    if "pipeline failed" in user_message:
        reply = "What error did you see?"
    elif "timeout" in user_message:
        reply = "Pipeline failed due to timeout. Check long-running jobs."
    elif "permission" in user_message:
        reply = "Pipeline failed due to permission issue. Check IAM roles."
    else:
        reply = "Can you provide more details?"

    return {"reply": reply}
