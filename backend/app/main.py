from fastapi import FastAPI
from .config import settings


from .database import engine, Base
from .api.cameras import router as camera_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.include_router(camera_router)#plugging the module into main application 

@app.get("/health")
def home():
    return {"message": "steelflow api is running"}