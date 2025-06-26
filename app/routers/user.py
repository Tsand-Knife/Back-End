# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud
from ..schemas import user as user_schemas
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register/", response_model=user_schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    created_user = crud.user.create_user(db=db, user=user)
    return created_user

@router.post("/login/", response_model=user_schemas.UserResponse)
def login_user_endpoint(user_credentials: user_schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.user.get_user_by_email(db, email=user_credentials.email)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # PENTING: Ganti ini dengan verifikasi password yang di-hash
    # Contoh sementara tanpa verifikasi hashing:
    if user.password != user_credentials.password + "notreallyhashed": # Ganti dengan verifikasi hashing yang aman
         raise HTTPException(status_code=400, detail="Incorrect email or password")

    # TODO: Implementasi token JWT untuk autentikasi setelah login berhasil
    return user

# Endpoint untuk mendapatkan user berdasarkan ID
@router.get("/{user_id}", response_model=user_schemas.UserResponse)
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Endpoint untuk mendapatkan semua user
@router.get("/", response_model=List[user_schemas.UserResponse])
def read_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.user.get_users(db, skip=skip, limit=limit)
    return users