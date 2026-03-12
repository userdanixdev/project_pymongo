import datetime
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.database.connection import client

# Banco:
db= client["project_mongo_test"]
# Coleção:
posts = db["posts"]
# Documento:
post = {
    "author":"Daniel",
    "text":"My first mongodb application based on Python",
    "tags":["mongodb","python3","pymongo"],
    "date": datetime.datetime.now(datetime.timezone.utc)
    },
{"author":"Daniela",
    "text":"My first mongodb application based on Python",
    "tags":["mongodb","python3","pymongo"],
    "date": datetime.datetime.now(datetime.timezone.utc)
}
# Inserir documento:
resultado = posts.insert_many(post)
print("Documento inserido:", resultado.inserted_ids)

