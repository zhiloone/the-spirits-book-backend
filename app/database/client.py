from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.settings import settings


class MongoDBClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = AsyncIOMotorClient(settings.DB_URI)
            cls._instance.db = cls._instance.client[settings.DB_NAME]
        return cls._instance

    @classmethod
    def get_database(cls) -> AsyncIOMotorDatabase:
        return cls().db  # Singleton instance ensures only one client exists
