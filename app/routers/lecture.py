from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud
from ..schemas import lecture as lecture_schemas
from ..database import get_db

router = APIRouter(
    prefix="/lectures",
    tags=["Lectures"]
)

@router.post("/", response_model=lecture_schemas.LectureResponse, status_code=status.HTTP_201_CREATED)
def create_lecture_endpoint(lecture: lecture_schemas.LectureCreate, db: Session = Depends(get_db)):
    return crud.lecture.create_lecture(db=db, lecture=lecture)

@router.get("/", response_model=List[lecture_schemas.LectureResponse])
def read_lectures_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lectures = crud.lecture.get_lectures(db, skip=skip, limit=limit)
    return lectures

@router.get("/{lecture_id}", response_model=lecture_schemas.LectureResponse)
def read_lecture_endpoint(lecture_id: int, db: Session = Depends(get_db)):
    db_lecture = crud.lecture.get_lecture(db, lecture_id=lecture_id)
    if db_lecture is None:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return db_lecture

@router.put("/{lecture_id}", response_model=lecture_schemas.LectureResponse)
def update_lecture_endpoint(lecture_id: int, lecture: lecture_schemas.LectureUpdate, db: Session = Depends(get_db)):
    db_lecture = crud.lecture.update_lecture(db, lecture_id=lecture_id, lecture_update=lecture)
    if db_lecture is None:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return db_lecture

@router.delete("/{lecture_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lecture_endpoint(lecture_id: int, db: Session = Depends(get_db)):
    db_lecture = crud.lecture.delete_lecture(db, lecture_id=lecture_id)
    if db_lecture is None:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return {"message": "Lecture deleted successfully"}
