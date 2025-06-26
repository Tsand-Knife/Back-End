from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud
from ..schemas import score as score_schemas
from ..database import get_db

router = APIRouter(
    prefix="/scores",
    tags=["Scores"]
)

@router.post("/", response_model=score_schemas.ScoreResponse, status_code=status.HTTP_201_CREATED)
def create_score_endpoint(score: score_schemas.ScoreCreate, db: Session = Depends(get_db)):
    # Optional: Anda bisa menambahkan validasi di sini untuk memastikan id_user dan id_topic itu ada
    # user_exists = crud.user.get_user(db, user_id=score.id_user)
    # if not user_exists:
    #     raise HTTPException(status_code=404, detail="User not found")
    # topic_exists = crud.topic.get_topic(db, topic_id=score.id_topic)
    # if not topic_exists:
    #     raise HTTPException(status_code=404, detail="Topic not found")
        
    return crud.score.create_score(db=db, score=score)

@router.get("/", response_model=List[score_schemas.ScoreResponse])
def read_scores_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    scores = crud.score.get_scores(db, skip=skip, limit=limit)
    return scores

@router.get("/{score_id}", response_model=score_schemas.ScoreResponse)
def read_score_endpoint(score_id: int, db: Session = Depends(get_db)):
    db_score = crud.score.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@router.put("/{score_id}", response_model=score_schemas.ScoreResponse)
def update_score_endpoint(score_id: int, score: score_schemas.ScoreUpdate, db: Session = Depends(get_db)):
    db_score = crud.score.update_score(db, score_id=score_id, score_update=score)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@router.delete("/{score_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_score_endpoint(score_id: int, db: Session = Depends(get_db)):
    db_score = crud.score.delete_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return {"message": "Score deleted successfully"}

# Endpoint tambahan untuk mendapatkan skor berdasarkan user_id
@router.get("/user/{user_id}", response_model=List[score_schemas.ScoreResponse])
def read_scores_by_user_endpoint(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    scores = crud.score.get_scores_by_user(db, user_id=user_id, skip=skip, limit=limit)
    return scores

# Endpoint tambahan untuk mendapatkan skor berdasarkan topic_id
@router.get("/topic/{topic_id}", response_model=List[score_schemas.ScoreResponse])
def read_scores_by_topic_endpoint(topic_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    scores = crud.score.get_scores_by_topic(db, topic_id=topic_id, skip=skip, limit=limit)
    return scores