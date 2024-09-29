from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base
from datetime import datetime

class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_path = Column(String)
    content_type = Column(String)
    size = Column(Integer)
    upload_time = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, index=True)  # If you want to associate files with users
    
    