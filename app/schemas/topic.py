from pydantic import BaseModel
from typing import Optional

# Schema untuk data yang dibutuhkan saat membuat topik baru
class TopicCreate(BaseModel):
    topic_name: str

    class Config:
        from_attributes = True

# Schema untuk data yang akan ditampilkan sebagai respons API
class TopicResponse(BaseModel):
    id_topic: int
    topic_name: str

    class Config:
        from_attributes = True

# Schema untuk update topic (optional fields)
class TopicUpdate(BaseModel):
    topic_name: Optional[str] = None