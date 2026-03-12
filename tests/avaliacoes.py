import sys
from pathlib import Path

# adiciona a raiz do projeto no sys.path para permitir `import src...`
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.database.connection import client  # agora funciona

def main():
    # 1) ping
    client.admin.command("ping")
    print(" Ping OK")

    # 2) listar bancos visíveis
    dbs = client.list_database_names()
    print("\n Bancos visíveis no cluster:")
    for name in dbs:
        print("-", name)

    # 3) escolher um db e listar coleções (troque se quiser)
    db_name = "project_mongo_test"
    db = client[db_name]
    cols = db.list_collection_names()
    print(f"\n Coleções em '{db_name}':")
    for c in cols:
        print("-", c)

    # 4) se existir coleção, mostra contagem e 1 documento ( necessário trocar também)
    col_name = "posts"  # <- Escolher a coleção aqui, nomeando-a.
    col = db[col_name]
    count = col.count_documents({})
    print(f"\nTotal de documentos em '{db_name}.{col_name}': {count}")

    one = col.find_one()
    print("\nPrimeiro documento (se existir):")
    print(one)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(" Erro:", e)