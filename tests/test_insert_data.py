import sys
from pathlib import Path

# permitir importar src
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.database.connection import client

db = client["meu_banco"]
usuarios = db["usuarios"]

dados = [
    {"nome": "Daniel", "idade": 30},
    {"nome": "Maria", "idade": 25},
    {"nome": "João", "idade": 40}
]

resultado = usuarios.insert_many(dados)

print("Documentos inseridos:")
print(resultado.inserted_ids)