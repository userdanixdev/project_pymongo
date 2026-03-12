# Arquivo de rotas da coleção 'posts':

from flask import Blueprint, request, jsonify
from bson import ObjectId
from src.database.connection import db
import datetime

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))

posts_pb = Blueprint("posts",__name__) # Modularizador de rotas usado na variável.
colecao = db["posts"]

def serializar_post(post):
    return {
        "id": str(post["_id"]),
        "author": post.get("author"),
        "text": post.get("text"),
        "tags": post.get("tags", []),
        "date": post.get("date").isoformat() if post.get("date") else None
    }

@posts_pb.route("/posts",methods=["GET"])
def listar_posts():
    posts = []
    for post in colecao.find():
        posts.append(serializar_post(post))
            
    return jsonify(posts),200

# Observação importante: O campo 'date' no Mongo vem como 'datetime', e JSON puro não entende 'datetime'
# diretamente.
# MongoDB usa ObjectId como identificador.
# Como JSON não reconhece esse tipo, precisamos convertê-lo para string.

# 
@posts_pb.route("/posts/<id>",methods=["GET"])
def buscar_post(id):
    try:
        post = colecao.find_one({"_id":ObjectId(id)})
        if not post:
            return jsonify({"erro: Post não encontrado"}), 404
        return jsonify({serializar_post(post)}), 200
    except Exception:
        return jsonify({"erro":"ID inválido"}),400

@posts_pb.route("/posts", methods = ["POST"])    
def criar_post():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400
    author = dados.get("author")
    text = dados.get("text")
    tags = dados.get("tags", [])

    if not author or not text:
        return jsonify({"erro": "Os campos 'author' e 'text' são obrigatórios"}), 400
    
    novo_post = {
        "author":author,
        "text":text,
        "tags":tags,
        "date":datetime.datetime.utcnow()

    }    
    resultado = colecao.insert_one(novo_post)

    post_criado = colecao.find_one({"_id": resultado.inserted_id})

    return jsonify({
            "mensagem": "Post criado com sucesso",
            "post": serializar_post(post_criado)
        }), 201

@posts_pb.route("/posts/<id>", methods=["PUT"])
def atualizar_post(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro":"JSON não enviado"}),400
    campos_atualizar =  {}
    if "author" in dados:
        campos_atualizar["author"]= dados["author"]
    if "text" in dados:
        campos_atualizar["text"]=dados["text"]        
    if "tags" in dados:
        campos_atualizar["tags"]=dados["tags"]        
    if not campos_atualizar:
        return jsonify({"erro": "Nenhum campo válido enviado para atualização"}), 400
    try:
        resultado = colecao.update_one(
            {"_id":ObjectId(id)},
            {"$set":campos_atualizar}
        )        
        if resultado.matched_count == 0:
            return jsonify({"erro":"post não encontrado"}), 404
        
        post_atualizado = colecao.find_one({"_id":ObjectId(id)})
        return jsonify({"mensagem":"Post atualizado com sucesso",
                        "post": serializar_post(post_atualizado)}),200
    except Exception:
        return jsonify({"erro":"ID inválido"}),400

@posts_pb.route("/posts/<id>", methods = ["DELETE"])    
def deletar_post(id):
    try: 
        resultado = colecao.delete_one({"_id": ObjectId(id)})
        if resultado.deleted_count == 0:
            return jsonify({"erro":"posta não encontrado"}),404
        return jsonify({"mensagem": "post deletado com sucesso"}),200
    except Exception:
        return jsonify({"ERRO":"ID inválido"}), 400
    



    