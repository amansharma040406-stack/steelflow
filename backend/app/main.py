from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .models.camera import Camera
from .database import SessionLocal, engine, Base
from .schemas.camera import CameraCreate, CameraResponse, CameraUpdate
from fastapi import FastAPI, Depends, HTTPException

Base.metadata.create_all(bind=engine)

app=FastAPI()
@app.get("/health")
def home():
    return{"message":"steeelflow api is running"}
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/cameras", response_model=list[CameraResponse])
def get_camera(db: Session = Depends(get_db)):
    cameras=db.query(Camera).all()
    result=[]
    for camera in cameras:
        result.append({
            "id":camera.id,
            "camera_uid":camera.camera_uid,
            "name":camera.name,
            "location":camera.location,
            "is_active":camera.is_active
        })
    return result
@app.post("/cameras")
def create_camera(camera: CameraCreate, db: Session = Depends(get_db)):
    new_camera = Camera(
        camera_uid=camera.camera_uid,
        name=camera.name,
        location=camera.location,
        is_active=camera.is_active
    )

    db.add(new_camera)
    db.commit()
    db.refresh(new_camera)

    return {
        "id": new_camera.id,
        "camera_uid": new_camera.camera_uid,
        "name": new_camera.name,
        "location": new_camera.location,
        "is_active": new_camera.is_active
    }

@app.post("/cameras")
def create_camera(camera: CameraCreate, db: Session = Depends(get_db)):

    new_camera = Camera(
        name=camera.name,
        location=camera.location,
        is_active=camera.is_active
    )

    db.add(new_camera)
    db.commit()
    db.refresh(new_camera)

    return {
        "id": new_camera.id,
        "name": new_camera.name,
        "location": new_camera.location,
        "is_active": new_camera.is_active
    }
@app.get("/cameras/{camera_id}", response_model=CameraResponse)
def get_camera_by_id(camera_id: int, db: Session = Depends(get_db)):

    camera = db.query(Camera).filter(Camera.id == camera_id).first()

    if camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")

    return camera

@app.put("/camera/{camera_id}", response_model=CameraResponse)
def update_camera(
    camera_id:int,
    camera_data:CameraUpdate,
    db:Session=Depends(get_db)

):
    camera = db.query(Camera).filter(Camera.id == camera_id).first()
    if camera is None:
            raise HTTPException(status_code=404, detail="Camera not found")
    camera.name = camera_data.name
    camera.location=camera_data.location
    camera.is_active=camera_data.is_active

    db.commit()
    db.refresh(camera)

    return camera

