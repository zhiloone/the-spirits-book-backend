from typing import Optional
from pydantic import BaseModel, Field


class QuestionTextModel(BaseModel):
    letter: Optional[str] = Field(example="a")
    question: Optional[list[str]] = Field(
        example=["Que definição podeis dar da matéria?"]
    )
    answer: list[str] = Field(
        example=[
            "A matéria é o laço que prende o espírito; é o instrumento de que este se serve e sobre o qual, ao mesmo tempo, exerce sua ação."
        ]
    )
    authors: Optional[list[str]] = Field(example=["São Luís", "Santo Agostinho"])


class QuestionModel(BaseModel):
    id: Optional[int] = Field(alias="_id", default=None)
    part: str = Field(example="Parte Primeira: Das causas primárias")
    chapter: str = Field(example="Capítulo I: De Deus")
    section: str = Field(example="Deus e o Infinito")
    questions: list[QuestionTextModel] = Field()
    comment: Optional[str] = Field(example="Comentário sobre a questão")
