import sys
from pathlib import Path
import datetime

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.database.connection import client

db = client["project_mongo_test"]
# coleção:
carros = db["carros"]
# Documento:
post = {"author": "Daniel",
    "text": "My first mongodb application based on Python - Cars",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.now(datetime.timezone.utc)}

# Inserir documento:

resultado = carros.insert_one(post)
print("Documento Inserido: \n", resultado.inserted_id)