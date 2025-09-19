import uuid
from sqlalchemy import Column, Date, TIMESTAMP, Numeric, Text, Boolean, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB, INET
from app.database import Base
from sqlalchemy.sql import func

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    location_id = Column(Integer, ForeignKey("work_locations.id"), nullable=False)
    attendance_date = Column(Date, nullable=False)

    # Clock in
    clock_in_time = Column(TIMESTAMP(timezone=True))
    clock_in_latitude = Column(Numeric(10,8))
    clock_in_longitude = Column(Numeric(11,8))
    clock_in_address = Column(Text)
    clock_in_photo = Column(String(255))
    clock_in_distance_meters = Column(Numeric(8,2))
    clock_in_valid = Column(Boolean, default=False)

    # Clock out
    clock_out_time = Column(TIMESTAMP(timezone=True))
    clock_out_latitude = Column(Numeric(10,8))
    clock_out_longitude = Column(Numeric(11,8))
    clock_out_address = Column(Text)
    clock_out_photo = Column(String(255))
    clock_out_distance_meters = Column(Numeric(8,2))
    clock_out_valid = Column(Boolean, default=False)

    # status & metrics
    status = Column(String(20), default="hadir")
    total_work_hours = Column(Numeric(4,2), default=0)
    overtime_hours = Column(Numeric(4,2), default=0)
    late_minutes = Column(Integer, default=0)
    notes = Column(Text)

    device_info = Column(JSONB)
    ip_address = Column(INET)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = ()
