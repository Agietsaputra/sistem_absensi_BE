from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP
from app.database import Base
from sqlalchemy.sql import func

class SystemSetting(Base):
    __tablename__ = "system_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    setting_key = Column(String(100), unique=True, nullable=False)
    setting_value = Column(Text, nullable=False)
    description = Column(Text)
    category = Column(String(50), default="general")
    data_type = Column(String(20), default="string")
    is_editable = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
