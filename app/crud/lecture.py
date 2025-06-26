from sqlalchemy.orm import Session
from ..model import lecture as lecture_model
from ..schemas import lecture as lecture_schemas

def get_lecture(db: Session, lecture_id: int):
    return db.query(lecture_model.Lecture).filter(lecture_model.Lecture.id_lecture == lecture_id).first()

def get_lecture_by_name(db: Session, lecture_name: str):
    return db.query(lecture_model.Lecture).filter(lecture_model.Lecture.lecture_name == lecture_name).first()

def get_lectures(db: Session, skip: int = 0, limit: int = 100):
    return db.query(lecture_model.Lecture).offset(skip).limit(limit).all()

# Fungsi untuk membuat materi baru
def create_lecture(db: Session, lecture: lecture_schemas.LectureCreate):
    db_lecture = lecture_model.Lecture(
        lecture_name=lecture.lecture_name,
        content=lecture.content
        # id_topic=lecture.id_topic # Hapus atau komentari ini
    )
    db.add(db_lecture)
    db.commit()
    db.refresh(db_lecture)
    return db_lecture

# Fungsi untuk memperbarui materi
def update_lecture(db: Session, lecture_id: int, lecture_update: lecture_schemas.LectureUpdate):
    db_lecture = db.query(lecture_model.Lecture).filter(lecture_model.Lecture.id_lecture == lecture_id).first()
    if db_lecture:
        for key, value in lecture_update.dict(exclude_unset=True).items():
            setattr(db_lecture, key, value)
        db.commit()
        db.refresh(db_lecture)
    return db_lecture

# Fungsi untuk menghapus materi
def delete_lecture(db: Session, lecture_id: int):
    db_lecture = db.query(lecture_model.Lecture).filter(lecture_model.Lecture.id_lecture == lecture_id).first()
    if db_lecture:
        db.delete(db_lecture)
        db.commit()
    return db_lecture