from datetime import date
from fastapi import APIRouter

from app.questions.models import QuestionModel
from app.questions.service import get_daily_question, get_question


router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get(
    "/daily",
    response_description="Get the question of the day",
    response_model=QuestionModel,
    response_model_by_alias=False,
)
async def get_daily_question_route(requested_date: date = None):
    return await get_daily_question(requested_date)


@router.get(
    "/{id}",
    response_description="Get a single question",
    response_model=QuestionModel,
    response_model_by_alias=False,
)
async def get_question_route(id: int):
    return await get_question(id)
