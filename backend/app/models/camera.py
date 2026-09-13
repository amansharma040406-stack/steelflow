from sqlalchemy import Column, Integer, String, Boolean
from backend.app.database import Base
class Camera(Base):
    __tablename__ ="cameras"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    location=Column(String, nullable=False)
    is_active=Column(Boolean, default=True)
