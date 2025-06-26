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


    class Config:
        from_attributes = True

# Schema untuk update score (optional fields)
class ScoreUpdate(BaseModel):
    score: Optional[int] = None