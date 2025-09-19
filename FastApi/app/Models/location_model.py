from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class WorkLocation(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    latitude = Column(Numeric(10,8), nullable=False)
    longitude = Column(Numeric(11,8), nullable=False)
    radius_meters = Column(Integer, default=100, nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
