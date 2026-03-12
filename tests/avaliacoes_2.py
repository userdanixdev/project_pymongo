import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

from src.database.connection import client

def main():
    # Conferir Conexão (PING):
    client.admin.command("ping")
    print("Ping OK")

    # Listar bancos disponíveis:
    dbs = client.list_database_names()
    print("Bancos visíveis no cluster:")
    for name in dbs:
        print("-", name)

    while True:    
        # Escolher banco
        db_name = input("\nDigite o nome do banco: ").strip()
        if db_name not in dbs:
            print(" Banco não existe no MongoDB")
            continue
        # Acessar banco:
        db= client[db_name]
        # Listar coleções:
        cols = db.list_collection_names()
        print(f"\n Coleções em '{db_name}':")
        if not cols:
            print("Nenhuma coleção encontrada")
            continue
        for c in cols:
            print("-", c)
        # Escolher coleção ( if exists )            
        col_name = input("\n Digite o nome da coleção: ").strip()
        if col_name not in cols:
            print("Coleção não existe nesse banco.")
            continue
        # Acessar coleção:
        colecao = db[col_name]        
        # Buscar documentos:
        documentos = colecao.find()
        print(f"\n Documentos da coleção: '{col_name}':")
        tem_dados = False
        for doc in documentos:
            print(doc)
            tem_dados = True
        if not tem_dados:
            print("Nenhuma documento encontrado")        
        # Opção voltar ou sair:
        opcao = input("\n Digite [V] para VOLTAR.\n [S] para sair: ").strip().lower()
        if opcao == "s":
            print("Encerrando programa...")
            break

if __name__ == "__main__":
    main()

