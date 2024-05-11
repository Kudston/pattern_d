from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from src.config import Settings

app = FastAPI()

app_settings = Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings.allowed_origins,
    allow_credentials=app_settings.allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(TrustedHostMiddleware, allowed_hosts=app_settings.allowed_hosts)

@app.get("/")
async def welcome():
    return {"detail":"Welcome to patternDetector"}