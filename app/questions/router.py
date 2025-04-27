from fastapi import APIRouter

from app.questions.models import QuestionModel
from app.questions.service import get_question


router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get(
    "/{id}",
    response_description="Get a single question",
    response_model=QuestionModel,
    response_model_by_alias=False,
)
async def get_question_route(id: int):
    return await get_question(id)
