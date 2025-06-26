from sqlalchemy.orm import Session
from ..model import user as user_model
from ..schemas import user as user_schemas

def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id_user == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_schemas.UserCreate):
    # PENTING: Anda HARUS mengganti ini dengan hashing password yang aman di produksi
    # Contoh sederhana tanpa hashing (TIDAK DIREKOMENDASIKAN untuk produksi):
    fake_hashed_password = user.password + "notreallyhashed" # Contoh: HASHING AKAN DILAKUKAN DI SINI
    
    db_user = user_model.User(
        email=user.email,
        password=fake_hashed_password, # Ini harus password yang sudah di-hash
        name=user.name,
        role=user.role # Menggunakan nilai boolean dari input
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: user_schemas.UserUpdate):
    db_user = db.query(user_model.User).filter(user_model.User.id_user == user_id).first()
    if db_user:
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(user_model.User).filter(user_model.User.id_user == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user