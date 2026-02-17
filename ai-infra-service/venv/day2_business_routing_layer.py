from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#This will check the input request validation
class DebugRequest(BaseModel):
    message: str

#This will check the response request validation
class DebugResponse(BaseModel):
    REPLY: str

#This is the business logic , line (message: str) -> str: means the input and output will be string only
def process_debug_message(message: str) -> str: 
    message = message.lower()

    if "pipeline failed" in message:
        return "What error did you see?"
    elif "timeout" in message:
        return "Pipeline failed due to timeout. Check long-running jobs."
    elif "permission" in message:
        return "Pipeline failed due to permission issue. Check IAM roles."
    else:
        return "Can you provide more details?"

#This is the routing layer which will handle the HTTP request 
@app.post("/debug", response_model=DebugResponse)
def debug(request: DebugRequest):
    reply = process_debug_message(request.message)
    return {"REPLY": reply}
