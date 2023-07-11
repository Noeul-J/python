import os
from typing import Optional
from fastapi import FastAPI
from routes.test import router as test_router

app = FastAPI()
app.include_router(test_router)


@app.get('/')
def index():
    return {
        "Python": "Framework",
    }