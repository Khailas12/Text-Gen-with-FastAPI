from fastapi import FastAPI

from gen import schemas
from .routers import gen_text
from .repository.gen import async_gen_text, models as multiple_models


app = FastAPI()

app.include_router(gen_text.router)


models = {}

@app.on_event("startup")
async def startup():
    # This function runs when the application starts.
    # It initializes the global `models` variable with preloaded models (e.g., machine learning models).
    global models
    models = multiple_models  # Load the models into memory during startup

@app.on_event("shutdown")
async def shutdown():
    # This function runs when the application shuts down.
    # It clears the `models` variable to release memory and clean up resources.
    global models
    models = {}  # Clear the models from memory
