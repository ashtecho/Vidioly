"""Vidioly Backend — main entry point."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api.routes import router
from config.settings import OUTPUT_DIR, PORT

# Create output dir
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = FastAPI(
    title="Vidioly API",
    description="Faceless YouTube video generator",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "name":    "Vidioly API",
        "version": "1.0.0",
        "status":  "running ✅",
        "docs":    "/docs",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
