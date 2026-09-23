from fastapi import FastAPI

from .database import engine, Base
from .api.cameras import router as camera_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(camera_router)#plugging the module into main application 

@app.get("/health")
def home():
    return {"message": "steelflow api is running"}