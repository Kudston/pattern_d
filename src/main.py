from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from src.config import Settings
from src.database import sessionLocal, engine
from src.models import TestModel
from src import models

models.Base.metadata.create_all(bind=engine)

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

new_session = sessionLocal()
db_obj = TestModel(title="first_object")
new_session.add(db_obj)
new_session.commit()
new_session.refresh(db_obj)

@app.get("/")
async def welcome():
    return {"detail":"Welcome to patternDetector"}

@app.get("/get_objs")
async  def get_objs():
    all = new_session.query(TestModel).all()
    return {'objects':all}
