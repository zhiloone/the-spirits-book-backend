from fastapi import HTTPException, status
from app.database import MongoDBClient


db = MongoDBClient.get_database()
question_collection = db["questions"]


async def get_question(id: int):
    evidence = await question_collection.find_one({"_id": id})

    if not evidence:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question {id} not found",
        )

    return evidence
