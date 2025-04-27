import json
import tqdm

from app.database.client import MongoDBClient


# TODO: test me (talvez pegar direto de uma const python seja melhor? daí já usa o pydantic)
def seed_questions(file_path):
    db = MongoDBClient.get_database()
    collection = db["questions"]

    # Lê o arquivo JSON com as perguntas
    with open(file_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    # Agora insere as perguntas no banco de dados
    for question in tqdm.tqdm(questions, desc="Seeding Questions", unit="question"):
        question_doc = {
            "part": question.get("part"),
            "chapter": question.get("chapter"),
            "section": question.get("section"),
            "question": question.get("question"),
            "answer": question.get("answer", []),
            "subquestions": question.get("subquestions", []),
            "comment": question.get("comment", ""),
            "author": question.get("author", ""),
        }

        # Inserindo o documento na coleção
        collection.insert_one(question_doc)

    print("Seeding completed.")


# Chama a função passando o caminho para o arquivo JSON
seed_questions("questions.json")
