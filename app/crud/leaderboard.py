from sqlalchemy.orm import Session
from sqlalchemy import func # Import func untuk agregasi
from ..model import leaderboard as leaderboard_model
from ..model import user as user_model
from ..model import topic as topic_model
from ..model import score as score_model # Bisa diimport jika perlu menghitung dari scores
from ..schemas import leaderboard as leaderboard_schemas

def get_leaderboard_entry(db: Session, lb_id: int):
    return db.query(leaderboard_model.Leaderboard).filter(leaderboard_model.Leaderboard.id_lb == lb_id).first()

def get_leaderboard_by_topic(db: Session, topic_id: int, skip: int = 0, limit: int = 100):
    # Mengambil leaderboard untuk topik tertentu, diurutkan berdasarkan skor dan posisi
    return db.query(leaderboard_model.Leaderboard)\
        .filter(leaderboard_model.Leaderboard.id_topic == topic_id)\
        .order_by(leaderboard_model.Leaderboard.position.asc(), leaderboard_model.Leaderboard.score.desc())\
        .offset(skip).limit(limit).all()

def get_overall_leaderboard(db: Session, skip: int = 0, limit: int = 100):
    # Mengambil leaderboard keseluruhan (mungkin agregasi skor total dari semua topik)
    # Ini adalah contoh yang lebih kompleks, bisa diimplementasikan nanti
    # Misalnya: mengagregasi skor dari tabel 'scores'
    overall_scores = db.query(
        score_model.Score.id_user,
        func.sum(score_model.Score.score).label('total_score')
    )\
    .group_by(score_model.Score.id_user)\
    .order_by(func.sum(score_model.Score.score).desc())\
    .offset(skip).limit(limit).all()

    # Anda perlu mapping ini ke schema atau membuat objek Leaderboard sementara
    # Atau, tabel leaderboard Anda memang sudah menyimpan agregasi ini.
    # Untuk sementara, jika Leaderboard table menyimpan per topik, fungsi ini perlu disesuaikan
    # atau memang Leaderboard table dirancang untuk skor agregat.

    # Untuk skema tabel Leaderboard Anda saat ini (per topik), kita bisa ambil semua entri:
    return db.query(leaderboard_model.Leaderboard)\
        .order_by(leaderboard_model.Leaderboard.position.asc(), leaderboard_model.Leaderboard.score.desc())\
        .offset(skip).limit(limit).all()


def create_leaderboard_entry(db: Session, entry: leaderboard_schemas.LeaderboardCreate):
    # Logika untuk menentukan 'position' mungkin ada di sini
    # Misalnya, Anda bisa menghitung posisi berdasarkan skor saat ini untuk topik yang sama
    # Atau, jika 'position' sudah dikirim dari frontend, langsung gunakan.

    db_entry = leaderboard_model.Leaderboard(
        id_user=entry.id_user,
        id_topic=entry.id_topic,
        score=entry.score,
        position=entry.position # Hati-hati dengan ini, idealnya dihitung backend
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def update_leaderboard_entry(db: Session, lb_id: int, entry_update: leaderboard_schemas.LeaderboardUpdate):
    db_entry = db.query(leaderboard_model.Leaderboard).filter(leaderboard_model.Leaderboard.id_lb == lb_id).first()
    if db_entry:
        for key, value in entry_update.dict(exclude_unset=True).items():
            setattr(db_entry, key, value)
        db.commit()
        db.refresh(db_entry)
    return db_entry

def delete_leaderboard_entry(db: Session, lb_id: int):
    db_entry = db.query(leaderboard_model.Leaderboard).filter(leaderboard_model.Leaderboard.id_lb == lb_id).first()
    if db_entry:
        db.delete(db_entry)
        db.commit()
    return db_entry