from pydantic import BaseModel


class CameraCreate(BaseModel):
    camera_uid: str
    name: str
    location: str
    is_active: bool = True


class CameraResponse(BaseModel):
    id: int
    camera_uid: str
    name: str
    location: str
    is_active: bool
    