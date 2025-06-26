from pydantic import BaseModel
from typing import Optional

# Untuk respons API yang juga menyertakan detail user dan topic
from .user import UserResponse  # Import UserResponse schema
from .topic import TopicResponse # Import TopicResponse schema

# Schema untuk data yang dibutuhkan saat membuat score baru
class ScoreCreate(BaseModel):
    id_user: int
    id_topic: int
    score: int # Nilai skor

    class Config:
        from_attributes = True

# Schema untuk data yang akan ditampilkan sebagai respons API
class ScoreResponse(BaseModel):
    id_score: int
    id_user: int
    id_topic: int
    score: int

    # Jika Anda ingin mengembalikan objek User dan Topic di dalam ScoreResponse
    # user: UserResponse # Uncoment ini jika Anda mau responsnya detail user
    # topic: TopicResponse # Uncoment ini jika Anda mau responsnya detail topic

    class Config:
        from_attributes = True

# Schema untuk update score (optional fields)
class ScoreUpdate(BaseModel):
    score: Optional[int] = None
    # id_user: Optional[int] = None # Biasanya tidak diupdate
    # id_topic: Optional[int] = None # Biasanya tidak diupdate