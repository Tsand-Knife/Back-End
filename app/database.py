from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ganti dengan kredensial PostgreSQL Anda
# Format: "postgresql://user:password@host:port/dbname"
DATABASE_URL = "postgresql://postgres:Yamino0903@localhost:5432/thinkeddb" # Contoh. Pastikan ini sesuai!

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()