import uuid
from sqlalchemy import Column, Integer, Time, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy import UniqueConstraint

class WorkSchedule(Base):
    __tablename__ = "schedule"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    location_id = Column(Integer, ForeignKey("work_locations.id"), nullable=False)
    day_of_week = Column(Integer, nullable=False)  # 1..7
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    break_duration_minutes = Column(Integer, default=60)
    is_active = Column(Boolean, default=True)
    effective_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    __table_args__ = (UniqueConstraint("employee_id", "day_of_week", "effective_date", name="uq_schedule_emp_day_effective"),)
