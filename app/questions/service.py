from datetime import date
from typing import Optional
from fastapi import HTTPException, status
from app.database.client import MongoDBClient
from app.questions.utils import date_to_question_id


db = MongoDBClient.get_database()
question_collection = db["questions"]


async def get_question(id: int):
    question = await question_collection.find_one({"_id": id})

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question {id} not found",
        )

    return question


async def get_daily_question(requested_date: Optional[date]):
    if not requested_date:
        requested_date = date.today()

    total_questions = await question_collection.count_documents({})

    question_id = date_to_question_id(requested_date, total_questions)

    question = await get_question(question_id)
    return question
