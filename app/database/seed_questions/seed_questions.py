# seed_questions.py
from loguru import logger
from app.database.client import MongoDBClient
from app.database.seed_questions.batches import ALL_QUESTION_BATCHES
from app.questions.models import QuestionModel
import asyncio
from pymongo.errors import DuplicateKeyError


async def seed_questions():
    client = MongoDBClient()
    await client.check_connection()
    collection = client.get_database()["questions"]

    for batch in ALL_QUESTION_BATCHES:
        for question_data in batch:
            model = QuestionModel(
                # Convert "number" -> "id"
                id=question_data.get("number"),
                part=question_data.get("part"),
                chapter=question_data.get("chapter"),
                section=question_data.get("section"),
                questions=question_data.get("questions"),
                comment=question_data.get("comment"),
            )
            try:
                await collection.insert_one(
                    model.model_dump(by_alias=True, exclude_none=True)
                )
                logger.info(f"Inserted Question ID {model.id}")
            except DuplicateKeyError:
                logger.warning(f"Question ID {model.id} already exists")
                pass


if __name__ == "__main__":
    asyncio.run(seed_questions())
