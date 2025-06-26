from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud
from ..schemas import topic as topic_schemas # Menggunakan alias
from ..database import get_db

router = APIRouter(
    prefix="/topics",
    tags=["Topics"]
)

@router.post("/", response_model=topic_schemas.TopicResponse, status_code=status.HTTP_201_CREATED)
def create_topic(topic: topic_schemas.TopicCreate, db: Session = Depends(get_db)):
    db_topic = crud.topic.get_topic_by_name(db, topic_name=topic.topic_name)
    if db_topic:
        raise HTTPException(status_code=400, detail="Topic name already exists")
    return crud.topic.create_topic(db=db, topic=topic)

@router.get("/", response_model=List[topic_schemas.TopicResponse])
def read_topics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    topics = crud.topic.get_topics(db, skip=skip, limit=limit)
    return topics

@router.get("/{topic_id}", response_model=topic_schemas.TopicResponse)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    db_topic = crud.topic.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

@router.put("/{topic_id}", response_model=topic_schemas.TopicResponse)
def update_topic(topic_id: int, topic: topic_schemas.TopicUpdate, db: Session = Depends(get_db)):
    db_topic = crud.topic.update_topic(db, topic_id=topic_id, topic_update=topic)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

@router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_topic(topic_id: int, db: Session = Depends(get_db)):
    db_topic = crud.topic.delete_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return {"message": "Topic deleted successfully"}