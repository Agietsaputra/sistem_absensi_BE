import uuid
from sqlalchemy import Column, TIMESTAMP, Numeric, Text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB, INET
from app.database import Base
from sqlalchemy.sql import func

class AttendanceLog(Base):
    __tablename__ = "attendance_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    attendance_id = Column(UUID(as_uuid=True), ForeignKey("attendance.id", ondelete="CASCADE"), nullable=False)
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.id"), nullable=False)
    action_type = Column(String(20), nullable=False)  # clock_in, clock_out, manual_correction
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    latitude = Column(Numeric(10,8))
    longitude = Column(Numeric(11,8))
    address = Column(Text)
    distance_meters = Column(Numeric(8,2))
    photo = Column(String(255))
    device_info = Column(JSONB)
    ip_address = Column(INET)
    user_agent = Column(Text)
    is_valid = Column(Boolean, default=True)
    notes = Column(Text)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
