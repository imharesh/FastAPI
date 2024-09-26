# models.py

import uuid
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.dialects.postgresql import UUID as pgUUID

class User(Base):
    __tablename__ = "users"
    id = Column(
        pgUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    businesses = relationship("Business", back_populates="owner")


class Product(Base):
    __tablename__ = "products"
    id = Column(
        pgUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    business_id = Column(pgUUID(as_uuid=True), ForeignKey("businesses.id"))

    business = relationship("Business", back_populates="products")


class Business(Base):
    __tablename__ = "businesses"
    id = Column(
        pgUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )
    name = Column(String, index=True)
    location = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    owner_name = Column(String, index=True)
    owner_id = Column(pgUUID(as_uuid=True), ForeignKey("users.id"))

    owner = relationship("User", back_populates="businesses")
    products = relationship("Product", back_populates="business")
