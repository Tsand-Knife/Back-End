from sqlalchemy.orm import Session
from ..model import score as score_model
from ..schemas import score as score_schemas

def get_score(db: Session, score_id: int):
    return db.query(score_model.Score).filter(score_model.Score.id_score == score_id).first()

def get_scores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(score_model.Score).offset(skip).limit(limit).all()

def get_scores_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(score_model.Score).filter(score_model.Score.id_user == user_id).offset(skip).limit(limit).all()

def get_scores_by_topic(db: Session, topic_id: int, skip: int = 0, limit: int = 100):
    return db.query(score_model.Score).filter(score_model.Score.id_topic == topic_id).offset(skip).limit(limit).all()

def create_score(db: Session, score: score_schemas.ScoreCreate):
    db_score = score_model.Score(
        id_user=score.id_user,
        id_topic=score.id_topic,
        score=score.score
    )
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def update_score(db: Session, score_id: int, score_update: score_schemas.ScoreUpdate):
    db_score = db.query(score_model.Score).filter(score_model.Score.id_score == score_id).first()
    if db_score:
        for key, value in score_update.dict(exclude_unset=True).items():
            setattr(db_score, key, value)
        db.commit()
        db.refresh(db_score)
    return db_score

def delete_score(db: Session, score_id: int):
    db_score = db.query(score_model.Score).filter(score_model.Score.id_score == score_id).first()
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score