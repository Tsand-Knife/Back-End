from fastapi import FastAPI
from .routers import topic as topic_router
from .routers import lecture as lecture_router
from .routers import user as user_router
from .routers import score as score_router
from .routers import leaderboard as leaderboard_router
from .database import engine, Base

from .model import user, topic, lecture, score, leaderboard  # import model

app = FastAPI(
    title="ThinkEd API",
    description="API untuk aplikasi pembelajaran mandiri ThinkEd",
    version="0.1.0"
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    print("Database tables created/checked.")


# Daftarkan router
app.include_router(topic_router.router)
app.include_router(lecture_router.router)
app.include_router(user_router.router)
app.include_router(score_router.router)
app.include_router(leaderboard_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to ThinkEd API!"}