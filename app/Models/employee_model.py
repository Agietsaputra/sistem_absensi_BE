import uuid
from sqlalchemy import Column, String, Text, Date, Boolean, Numeric, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from sqlalchemy.sql import func

class Employee(Base):
    __tablename__ = "employees"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    employee_id = Column(String(20), unique=True, nullable=False)
    full_name = Column(String(200), nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    department = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    hire_date = Column(Date, nullable=False)
    salary = Column(Numeric(12,2))
    photo_profile = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
