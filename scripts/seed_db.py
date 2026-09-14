from backend.app.database import SessionLocal, Base, engine
from backend.app.models.camera import Camera

Base.metadata.create_all(bind=engine)

db = SessionLocal()

camera1 = Camera(
    id=1,
    name="camera 1",
    location="gate A",
    is_active=True
)

camera2 = Camera(
    id=2,
    name="camera 2",
    location="gate B",
    is_active=True
)

db.add(camera1)
db.add(camera2)

db.commit()
db.close()

print("Cameras added successfully!")