from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from .models.camera import Camera
from .schemas.camera import CameraCreate, CameraResponse, CameraUpdate


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Health Check

@app.get("/health")
def home():
    return {"message": "steelflow api is running"}

# Database Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# GET ALL CAMERAS
@app.get("/cameras", response_model=list[CameraResponse])
def get_camera(db: Session = Depends(get_db)):

    cameras = db.query(Camera).all()

    return cameras

# CREATE CAMERA
@app.post("/cameras", response_model=CameraResponse)
def create_camera(
    camera: CameraCreate,
    db: Session = Depends(get_db)
):

    new_camera = Camera(
        camera_uid=camera.camera_uid,
        name=camera.name,
        location=camera.location,
        is_active=camera.is_active
    )

    db.add(new_camera)
    db.commit()
    db.refresh(new_camera)

    return new_camera


# GET CAMERA BY ID
@app.get("/cameras/{camera_id}", response_model=CameraResponse)
def get_camera_by_id(
    camera_id: int,
    db: Session = Depends(get_db)
):

    camera = db.query(Camera).filter(Camera.id == camera_id).first()

    if camera is None:
        raise HTTPException(
            status_code=404,
            detail="Camera not found"
        )

    return camera


# UPDATE CAMERA
@app.put("/cameras/{camera_id}", response_model=CameraResponse)
def update_camera(
    camera_id: int,
    camera_data: CameraUpdate,
    db: Session = Depends(get_db)
):

    camera = db.query(Camera).filter(Camera.id == camera_id).first()

    if camera is None:
        raise HTTPException(
            status_code=404,
            detail="Camera not found"
        )

    camera.name = camera_data.name
    camera.location = camera_data.location
    camera.is_active = camera_data.is_active

    db.commit()
    db.refresh(camera)

    return camera

#delete camera:
@app.delete("/cameras/{camera_id}")
def delete_camera(
    camera_id: int,
    db: Session = Depends(get_db)
):
    camera = db.query(Camera).filter(Camera.id == camera_id).first()

    if camera is None:
        raise HTTPException(
            status_code=404,
            detail="Camera not found"
        )

    db.delete(camera)
    db.commit()

    return {
        "message": "Camera deleted successfully",
        "camera_id": camera_id
    }
    