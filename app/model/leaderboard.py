from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from .user import User # Import model User
from .topic import Topic # Import model Topic

class Leaderboard(Base):
    __tablename__ = "tbleaderboard" # Atau "tbleaderboard" jika Anda ingin konsisten dengan nama tabel di DB Anda

    id_lb = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=True) #ganti false nanti kalo udah isi db
    id_topic = Column(Integer, ForeignKey("topics.id_topic"), nullable=True) #ganti false nanti kalo udah isi db
    score = Column(Integer, nullable=True)
    position = Column(Integer, nullable=True) # Posisi peringkat di leaderboard

    # Definisikan relasi dengan User
    user = relationship("User", back_populates="leaderboards") # Perhatikan nama back_populates
    # Definisikan relasi dengan Topic
    topic = relationship("Topic", back_populates="leaderboards") # Perhatikan nama back_populates

    def __repr__(self):]
        return f"<Leaderboard(id_lb={self.id_lb}, id_user={self.id_user}, id_topic={self.id_topic}, score={self.score}, position={self.position})>"