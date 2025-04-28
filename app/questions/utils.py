from datetime import date
import hashlib


def date_to_question_id(date: date, total_questions: int) -> int:
    date_str = date.strftime("%Y-%m-%d")
    # Use the hash to transform date to a number
    hash_object = hashlib.sha256(date_str.encode())
    hash_int = int(hash_object.hexdigest(), 16)
    # and then map it to the range of question IDs
    return (hash_int % total_questions) + 1
