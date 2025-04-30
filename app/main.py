from fastapi import Depends, FastAPI

from app.auth import check_api_key

from app.questions.router import router as questions_router
from fastapi.middleware.cors import CORSMiddleware
from app.settings import settings

app = FastAPI(root_path="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://olivrodosespiritos.zhiloone.com.br/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if settings.ENVIRONMENT != "production":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/health")
def get_health():
    return "ok"


app.include_router(questions_router, dependencies=[Depends(check_api_key)])
