from fastapi import FastAPI
import time
import asyncio

app = FastAPI()


# ------------------------
# Simulated Slow Operation
# ------------------------

def slow_sync_operation():
    print("Sync operation started")
    time.sleep(3)
    print("Sync operation finished")
    return "Sync operation finished"


async def slow_async_operation():
    print("Async operation started")
    await asyncio.sleep(3)
    print("Async operation finished")
    return "Async operation finished"


# ------------------------
# Routes with Timing Logs
# ------------------------

@app.get("/sync")
def sync_route():
    start = time.time()
    result = slow_sync_operation()
    total_time = time.time() - start
    print(f"SYNC total execution time: {total_time:.4f} seconds")
    return {"message": result}


@app.get("/async")
async def async_route():
    start = time.time()
    result = await slow_async_operation()
    total_time = time.time() - start
    print(f"ASYNC total execution time: {total_time:.4f} seconds")
    return {"message": result}
