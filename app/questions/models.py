from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


def default_factory_now_tz():
    return datetime.now(timezone.utc)


class QuestionTextModel(BaseModel):
    letter: Optional[str] = Field(example="a", default=None)
    question: Optional[list[str]] = Field(
        example=["Que definição podeis dar da matéria?"], default=None
    )
    answer: list[str] = Field(
        example=[
            "A matéria é o laço que prende o espírito; é o instrumento de que este se serve e sobre o qual, ao mesmo tempo, exerce sua ação."
        ]
    )
    authors: Optional[list[str]] = Field(
        example=["São Luís", "Santo Agostinho"], default=None
    )


class QuestionModel(BaseModel):
    id: Optional[int] = Field(alias="_id", default=None)
    part: str = Field(example="Parte Primeira: Das causas primárias")
    chapter: str = Field(example="Capítulo I: De Deus")
    section: str = Field(example="Deus e o Infinito")
    questions: list[QuestionTextModel] = Field()
    comment: Optional[list[str]] = Field(
        example=["Comentário sobre a questão"], default=None
    )
    created_at: datetime = Field(
        default_factory=default_factory_now_tz, example=default_factory_now_tz()
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
