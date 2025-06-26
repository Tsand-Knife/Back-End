from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud
from ..schemas import leaderboard as leaderboard_schemas
from ..database import get_db

router = APIRouter(
    prefix="/leaderboard", # Prefix untuk semua endpoint di router ini
    tags=["Leaderboard"]
)

@router.post("/", response_model=leaderboard_schemas.LeaderboardResponse, status_code=status.HTTP_201_CREATED)
def create_leaderboard_entry_endpoint(
    entry: leaderboard_schemas.LeaderboardCreate,
    db: Session = Depends(get_db)
):
    # Optional: Anda bisa menambahkan validasi di sini untuk memastikan id_user dan id_topic ada
    # Misalnya:
    # user_exists = crud.user.get_user(db, user_id=entry.id_user)
    # if not user_exists:
    #     raise HTTPException(status_code=404, detail="User not found")
    # topic_exists = crud.topic.get_topic(db, topic_id=entry.id_topic)
    # if not topic_exists:
    #     raise HTTPException(status_code=404, detail="Topic not found")
        
    return crud.leaderboard.create_leaderboard_entry(db=db, entry=entry)

@router.get("/topic/{topic_id}", response_model=List[leaderboard_schemas.LeaderboardResponse])
def get_leaderboard_by_topic_endpoint(
    topic_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    leaderboard_entries = crud.leaderboard.get_leaderboard_by_topic(db, topic_id=topic_id, skip=skip, limit=limit)
    return leaderboard_entries

@router.get("/overall", response_model=List[leaderboard_schemas.LeaderboardResponse])
def get_overall_leaderboard_endpoint(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    # Ini akan memanggil fungsi yang mengembalikan semua entri leaderboard
    # Untuk leaderboard keseluruhan yang sebenarnya, perlu ada logika agregasi yang lebih kompleks di CRUD
    overall_entries = crud.leaderboard.get_overall_leaderboard(db, skip=skip, limit=limit)
    return overall_entries


@router.get("/{lb_id}", response_model=leaderboard_schemas.LeaderboardResponse)
def get_leaderboard_entry_endpoint(lb_id: int, db: Session = Depends(get_db)):
    db_entry = crud.leaderboard.get_leaderboard_entry(db, lb_id=lb_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Leaderboard entry not found")
    return db_entry

@router.put("/{lb_id}", response_model=leaderboard_schemas.LeaderboardResponse)
def update_leaderboard_entry_endpoint(
    lb_id: int,
    entry: leaderboard_schemas.LeaderboardUpdate,
    db: Session = Depends(get_db)
):
    db_entry = crud.leaderboard.update_leaderboard_entry(db, lb_id=lb_id, entry_update=entry)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Leaderboard entry not found")
    return db_entry

@router.delete("/{lb_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leaderboard_entry_endpoint(lb_id: int, db: Session = Depends(get_db)):
    db_entry = crud.leaderboard.delete_leaderboard_entry(db, lb_id=lb_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Leaderboard entry not found")
    return {"message": "Leaderboard entry deleted successfully"}