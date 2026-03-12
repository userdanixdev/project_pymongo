from database.connection import client

# cria ou acessa o banco:
db = client["meu_banco"]

# cria ou acessa a coleção:
colecao = db["usuarios"]

# inserir documento:
colecao.insert_one({
    "nome": "Daniel",
    "cargo": "Engenharia de Dados"
})

print("Documento inserido com sucesso")


# Aqui o MongoDB irá criar o banco meu_banco, criar a coleção usuarios e inserir o documento.