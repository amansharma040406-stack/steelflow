from fastapi import FastAPI
from backend.app.models.camera import Camera 
app=FastAPI()
@app.get("/health")
def home():
    return{"message":"steeelflow api is running"}
@app.get("/cameras")
def get_camera():
    camera1=Camera(
        1,
        "camera 1",
        "gate A",
        True
    )
    camera2=Camera(
        2,
        "camera 2",
        "gate B",
        True
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
