from pydantic import BaseModel
from datetime import datetime

class UploadedFileCreate(BaseModel):
    filename: str
    file_path: str
    content_type: str
    size: int
    user_id: int

class UploadedFileOut(BaseModel):
    id: int
    filename: str
    content_type: str
    size: int
    upload_time: datetime
    user_id: int

    class Config:
        orm_mode = True
        