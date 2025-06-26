from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from .user import User # Import model User
from .topic import Topic # Import model Topic

class Score(Base):
    __tablename__ = "tbscores" # Atau "tbscpres" jika Anda ingin konsisten dengan nama tabel di DB Anda

    id_score = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)
    id_topic = Column(Integer, ForeignKey("topics.id_topic"), nullable=False)
    score = Column(Integer, nullable=False) # Nilai skor kuis

    # Definisikan relasi dengan User
    user = relationship("User", back_populates="scores")
    # Definisikan relasi dengan Topic
    topic = relationship("Topic", back_populates="scores")

    def __repr__(self):
        return f"<Score(id_score={self.id_score}, id_user={self.id_user}, id_topic={self.id_topic}, score={self.score})>"
