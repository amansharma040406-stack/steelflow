from fastapi import FastAPI
from .models.camera import Camera # . = current package (app)
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app=FastAPI()
@app.get("/health")
def home():
    return{"message":"steeelflow api is running"}
@app.get("/cameras")
def get_camera():
    db= SessionLocal()
    cameras=db.query(Camera).all()
    result=[]
    for camera in cameras:
        result.append({
            "id":camera.id,
            "name":camera.name,
            "location":camera.location,
            "is_active":camera.is_active
        })
    db.close()
    return result
