from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from typing import List
import os
from uuid import uuid4
from sqlalchemy.orm import Session
from database.database import get_db
from models.uploaded_file_model import UploadedFile
from schemas.uploaded_file_schemas import UploadedFileOut
from routes.auth import oauth2_scheme, read_users_me

router = APIRouter()

# Configure the upload directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-files/", response_model=List[UploadedFileOut], tags=["File Upload"])
async def upload_files(
    files: List[UploadFile] = File(...), 
    db: Session = Depends(get_db),
    current_user: dict = Depends(read_users_me)
):
    uploaded_files = []

    for file in files:
        try:
            # Generate a unique filename
            file_extension = os.path.splitext(file.filename)[1]
            unique_filename = f"{uuid4()}{file_extension}"
            file_path = os.path.join(UPLOAD_DIR, unique_filename)

            # Save the file
            with open(file_path, "wb") as buffer:
                content = await file.read()
                buffer.write(content)
            
            # Create database entry
            db_file = UploadedFile(
                filename=file.filename,
                file_path=file_path,
                content_type=file.content_type,
                size=len(content),
                user_id=current_user.id  # Changed from current_user["id"]
            )
            db.add(db_file)
            db.commit()
            db.refresh(db_file)
            
            uploaded_files.append(db_file)

        

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error uploading file {file.filename}: {str(e)}")

    return uploaded_files

