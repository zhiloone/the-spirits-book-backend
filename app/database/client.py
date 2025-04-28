from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.settings import settings

from loguru import logger


class MongoDBClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            try:
                cls._instance.client = AsyncIOMotorClient(
                    settings.DB_URI,
                    serverSelectionTimeoutMS=5000,  # 5s max pra selecionar servidor
                )
                cls._instance.db = cls._instance.client[settings.DB_NAME]
            except Exception as e:
                logger.exception(f"Failed to create MongoDB client: {e}")
                raise
        return cls._instance

    @classmethod
    async def check_connection(cls):
        try:
            logger.info("Checking MongoDB connection...")
            await cls._instance.client.admin.command("ping")
            logger.info("Successfully connected to MongoDB.")
        except Exception as e:
            logger.exception(f"MongoDB connection check failed: {e}")
            raise

    @classmethod
    def get_database(cls) -> AsyncIOMotorDatabase:
        return cls().db
