import sys
from pathlib import Path

# Permitir importar src:
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.database.connection import client

db = client["meu_banco"]
usuarios = db["usuarios"]

dados = [
    {"nome": "Thiago", "idade": 32},
    {"nome": "Junior", "idade": 20},
    {"nome": "Adelino", "idade": 85}
]

resultado = usuarios.insert_many(dados)

print("Documentos inseridos:")
print(resultado.inserted_ids)