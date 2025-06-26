from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema untuk data yang dibutuhkan saat membuat user baru (pendaftaran)
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    role: bool # Tipe boolean untuk role (0/1 admin/user)

    class Config:
        from_attributes = True

# Schema untuk data yang akan ditampilkan sebagai respons API (tidak menampilkan password)
class UserResponse(BaseModel):
    id_user: int
    email: EmailStr
    name: str
    role: bool

    class Config:
        from_attributes = True

# Schema untuk data login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[bool] = None