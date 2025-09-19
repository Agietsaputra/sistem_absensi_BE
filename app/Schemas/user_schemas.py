from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UserCreate(BaseModel):
    employee_id: str
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = "karyawan"

class UserOut(BaseModel):
    id: UUID
    employee_id: str
    username: str
    email: EmailStr
    role: str
