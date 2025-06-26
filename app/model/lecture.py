from sqlalchemy import Column, Integer, String, Text
# from sqlalchemy.orm import relationship # Tidak perlu jika tidak ada relasi ke Topic
from ..database import Base
# from .topic import Topic # Tidak perlu diimpor jika tidak ada relasi

class Lecture(Base):
    __tablename__ = "tblectures" # Pastikan nama tabel ini sesuai dengan "tblectures" di PostgreSQL Anda

    id_lecture = Column(Integer, primary_key=True, index=True)
    lecture_name = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=False)

    # Relasi dengan Topic dihapus karena tidak ada hubungan langsung
    # id_topic = Column(Integer, ForeignKey("topics.id_topic")) # Hapus atau komentari ini
    # topic = relationship("Topic", back_populates="lectures") # Hapus atau komentari ini

    def __repr__(self):
        return f"<Lecture(id_lecture={self.id_lecture}, lecture_name='{self.lecture_name}')>"

