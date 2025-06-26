from sqlalchemy import Column, Integer, String, Boolean # Import Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "tbusers" # Sesuaikan dengan nama tabel di PostgreSQL Anda (tbusers)

    id_user = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False) # Pastikan nama kolom di DB adalah 'password' atau 'pass'
    name = Column(String, nullable=False)
    role = Column(Boolean, nullable=False) # 1 untuk admin, 0 untuk siswa/user biasa

    # Jika nanti ada relasi dengan tabel lain (misalnya scores)
    scores = relationship("Score", back_populates="user")
    leaderboards = relationship("Leaderboard", back_populates="user")

    def __repr__(self):
        return f"<User(id_user={self.id_user}, email='{self.email}', role='{self.role}')>"