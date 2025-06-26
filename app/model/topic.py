from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Topic(Base):
    __tablename__ = "topics" # Pastikan nama tabel ini sesuai dengan yang Anda buat di PostgreSQL

    id_topic = Column(Integer, primary_key=True, index=True)
    topic_name = Column(String, unique=True, index=True, nullable=False)

    # Contoh relasi jika nanti ada materi yang terkait dengan topik
    # materials = relationship("Material", back_populates="topic")

    def __repr__(self):
        return f"<Topic(id_topic={self.id_topic}, topic_name='{self.topic_name}')>"
