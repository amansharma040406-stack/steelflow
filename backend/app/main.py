from fastapi import FastAPI
from .models.camera import Camera # . = current package (app)
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app=FastAPI()
@app.get("/health")
def home():
    return{"message":"steeelflow api is running"}
@app.get("/cameras")
def get_camera():
    camera1=Camera(
        id=1,
        name="camera 1",
        location="gate A",
        is_active=True
    )
    camera2= Camera(
        id=2,
        name="camera 2",
        location="gate B",
        is_active=True
    )
    return[
        {
            "id":camera1.id,
            "name":camera1.name,
            "location":camera1.location,
            "is_active":camera1.is_active
        },
        {
            "id":camera2.id,
            "name":camera2.name,
            "location":camera2.location,
            "is_active":camera2.is_active
        }
    ]
