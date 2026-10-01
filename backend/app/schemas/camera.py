from pydantic import BaseModel
from datetime import datetime


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
    created_at:datetime 

class CameraUpdate(BaseModel):
    name: str
    location: str
    is_active:bool= True