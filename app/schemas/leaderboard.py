from pydantic import BaseModel
from typing import Optional, List

# Untuk respons API yang juga menyertakan detail user dan topic jika diperlukan
from .user import UserResponse
from .topic import TopicResponse

# Schema untuk data yang dibutuhkan saat membuat entri leaderboard baru
# Catatan: 'position' biasanya dihitung di backend, jadi mungkin tidak perlu di 'Create'
class LeaderboardCreate(BaseModel):
    id_user: int
    id_topic: int
    score: int
    position: int # Jika Anda ingin backend mengirimkan ini secara eksplisit, atau hapus jika dihitung otomatis

    class Config:
        from_attributes = True

# Schema untuk data yang akan ditampilkan sebagai respons API
class LeaderboardResponse(BaseModel):
    id_lb: int
    id_user: int
    id_topic: int
    score: int
    position: int

    # Jika Anda ingin mengembalikan objek User dan Topic di dalam LeaderboardResponse
    # user: UserResponse
    # topic: TopicResponse

    class Config:
        from_attributes = True

# Schema untuk update entri leaderboard (opsional fields)
class LeaderboardUpdate(BaseModel):
    score: Optional[int] = None
    position: Optional[int] = None