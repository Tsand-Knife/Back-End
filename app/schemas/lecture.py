from pydantic import BaseModel
from typing import Optional

# Schema untuk data yang dibutuhkan saat membuat materi/lecture baru
class LectureCreate(BaseModel):
    lecture_name: str
    content: str

    class Config:
        from_attributes = True

# Schema untuk data yang akan ditampilkan sebagai respons API
class LectureResponse(BaseModel):
    id_lecture: int
    lecture_name: str
    content: str

    class Config:
        from_attributes = True

# Schema untuk update materi/lecture (optional fields)
class LectureUpdate(BaseModel):
    lecture_name: Optional[str] = None
    content: Optional[str] = None