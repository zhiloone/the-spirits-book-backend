import pdfplumber
import re
import json
from tqdm import tqdm

questions = []

with pdfplumber.open("livro_dos_espiritos.pdf") as pdf:
    all_text = ""
    for page in tqdm(pdf.pages, desc="Reading pages"):
        all_text += page.extract_text() + "\n"

# Regex para capturar perguntas e respostas
pattern = re.compile(r"(\d{1,4})\.\s+(.*?)\n(.*?)(?=\n\d{1,4}\.\s+|$)", re.DOTALL)
matches = pattern.findall(all_text)

print(f"\n🔍 Detected {len(matches)} questions.")

for number, question, answer in tqdm(matches, desc="Processing questions"):
    clean_question = " ".join(question.strip().split())
    clean_answer = " ".join(answer.strip().split())
    questions.append({
        "number": int(number),
        "question": clean_question,
        "answer": clean_answer
    })

# Exportar para JavaScript
with open("perguntas.js", "w", encoding="utf-8") as f:
    f.write("const perguntasLivroDosEspiritos = ")
    f.write(json.dumps(questions, ensure_ascii=False, indent=2))
    f.write(";\n")

print("\n✅ Exported to perguntas.js!")
