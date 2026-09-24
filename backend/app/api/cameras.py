from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..models.camera import Camera
from ..schemas.camera import CameraCreate, CameraResponse, CameraUpdate

router = APIRouter()

# GET ALL CAMERAS
@router.get("/cameras", response_model=list[CameraResponse])
def get_camera(db: Session = Depends(get_db)):

    cameras = db.query(Camera).all()

    return cameras


# POST CAMERA
@router.post("/cameras", response_model=CameraResponse)
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
@router.get("/cameras/{camera_id}", response_model=CameraResponse)
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
@router.put("/cameras/{camera_id}", response_model=CameraResponse)
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
@router.delete("/cameras/{camera_id}")
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
    