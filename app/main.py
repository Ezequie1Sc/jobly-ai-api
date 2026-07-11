from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.cv import router as cv_router
from app.routers.recommendations import router as recommendations_router
from app.routers.chat import router as chat_router

app = FastAPI(
    title="Jobly AI API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cv_router)
app.include_router(recommendations_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Jobly AI API funcionando"
    }