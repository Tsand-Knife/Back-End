from pydantic import BaseModel
from typing import Optional, List

# Untuk respons API yang juga menyertakan detail user dan topic jika diperlukan
from .user import UserResponse
from .topic import TopicResponse

class LeaderboardCreate(BaseModel):
    id_user: int
    id_topic: int
    score: int
    position: int # masih nggak yakin untuk ini

    class Config:
        from_attributes = True

# Schema untuk data yang akan ditampilkan sebagai respons API
class LeaderboardResponse(BaseModel):
    id_lb: int
    id_user: int
    id_topic: int
    score: int
    position: int

    # kalo mau nampilin User dan Topic di dalam LeaderboardResponse
    # user: UserResponse
    # topic: TopicResponse

    class Config:
        from_attributes = True

# Schema untuk update entri leaderboard (opsional fields)
class LeaderboardUpdate(BaseModel):
    score: Optional[int] = None
    position: Optional[int] = None