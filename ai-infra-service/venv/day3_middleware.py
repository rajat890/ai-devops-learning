from fastapi import FastAPI, Request
from pydantic import BaseModel
import time

app = FastAPI()


# -------------------------
# Request & Response Models
# -------------------------

class DebugRequest(BaseModel):
    message: str


class DebugResponse(BaseModel):
    reply: str


# -------------------------
# Middleware
# -------------------------

@app.middleware("http") # This will register the middleware layer for all HTTP request 
async def log_requests(request: Request, call_next): # Incoming request object 
    start_time = time.time() # Record the start time 

    print(f"\nIncoming Request: {request.method} {request.url}")

    response = await call_next(request) # This will foward the request to route and business logic and this will wait for the code to complete 

    process_time = time.time() - start_time # this will calculate the execution time 
    print(f"Completed in {process_time:.4f} seconds")
    print(f"Status Code: {response.status_code}")
    
    return response


# -------------------------
# Business Logic
# -------------------------

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


# -------------------------
# Routes
# -------------------------

@app.get("/")
def home():
    return {"message": "AI Infra Debug Service Running"}


@app.post("/debug", response_model=DebugResponse)
def debug(request: DebugRequest):
    reply = process_debug_message(request.message)
    return {"reply": reply}
