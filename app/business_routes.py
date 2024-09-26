# business_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Business, Product
from schemas import BusinessCreate, BusinessOut
from database import SessionLocal
from uuid import UUID


router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/business", response_model=BusinessOut, tags=["Business"])
def create_business(business: BusinessCreate, db: Session = Depends(get_db)):
    # Create the business with UUID
    db_business = Business(
        name=business.name, 
        location=business.location, 
        email=business.email, 
        owner_name=business.owner_name
    )
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    
    # Optionally add products for the business
    for product in business.products:
        db_product = Product(
            name=product.name, 
            description=product.description, 
            price=product.price,
            business_id=db_business.id  # Use UUID for business ID
        )
        db.add(db_product)
    
    db.commit()
    return db_business

@router.get("/business/{business_id}", response_model=BusinessOut, tags=["Business"])
def get_business(business_id: UUID, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business

@router.put("/business/{business_id}", response_model=BusinessOut, tags=["Business"])
def update_business(business_id: UUID, business_data: BusinessCreate, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    # Update business data
    business.name = business_data.name
    business.location = business_data.location
    business.email = business_data.email
    business.owner_name = business_data.owner_name
    
    db.commit()
    return business

@router.delete("/business/{business_id}", tags=["Business"])
def delete_business(business_id: UUID, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    db.delete(business)
    db.commit()
    return {"message": "Business deleted successfully"}