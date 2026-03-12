import sys
from pathlib import Path

# adiciona a raiz do projeto no sys.path para permitir `import src...`
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.database.connection import client
# Criação do banco:
db_2 = client["project_mongo_test"]
# Cria a coleção:
colecao = db_2["carros"]

# Lista de documentos ( cada dicionário é um documento no MongoDB )

carros = [{"marca":"Toyota","modelo":"Corolla", "ano":2010},
          {"marca":"Honda","modelo":"Civic","ano":2010},
          {"marca":"Ford","modelo":"Focus","ano":2018},
          {"marca":"Chevrolet","modelo":"Onix","ano":2018},
          {"marca":"Volkswagem","modelo":"Golf","ano":2022}
          ]

# Inserir todos os documentos:

resultado = colecao.insert_many(carros)
print(f"Documentos inseridos:\n", resultado.inserted_ids)

# Fluxo:

# Os carros é uma lista de dicionários, cada dicionário é um documento MongoDB.
# O 'insert_many()' insere todos de uma vez e 'inserted_ids' retorna os IDs criados automaticamente.

