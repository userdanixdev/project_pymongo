# Arquivo de rotas da coleção 'carros':

from flask import Blueprint, request, jsonify
from bson import ObjectId
from src.database.connection import db

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))

carros_pb = Blueprint("carros",__name__) # Modularizador de rotas usado na variável.
colecao = db["carros"]

def serializar_carro(carro):
    return {
        "id": str(carro["_id"]),
        "marca": carro.get("marca"),
        "modelo": carro.get("modelo"),
        "ano": carro.get("ano")
    }

@carros_pb.route("/carros",methods=["GET"])
def listar_carros():
    carros = []
    for carro in colecao.find():
        carros.append(serializar_carro(carro))
         
    return jsonify(carros),200

# MongoDB usa ObjectId como identificador.
# Como JSON não reconhece esse tipo, precisamos convertê-lo para string.

@carros_pb.route("/carros/<id>", methods = ["GET"])
def buscar_carro(id):
    try:
        carro = colecao.find_one({"_id": ObjectId(id)})
        if not carro:
            return jsonify({"erro":"Carro não encontrado"}), 404
        return jsonify(serializar_carro(carro)), 200
    except Exception:
        return jsonify({"erro":"ID inválido"}), 400

@carros_pb.route("/carros", methods =  ["POST"])    
def criar_carro():
    dados = request.get_json()
    if not dados:
        return jsonify({"ERRO":"JSON não enviado"}),400
    marca = dados.get("marca")
    modelo = dados.get("modelo")
    ano = dados.get("ano")
    if not marca or not modelo or ano is None:
        return jsonify ({"erro":"Os campos 'marca','modelo' e 'ano' são obrigatórios"}), 400
    novo_carro = {
        "marca":marca,
        "modelo":modelo,
        "ano":ano
    }
    resultado = colecao.insert_one(novo_carro)
    carro_criado = colecao.find_one({"_id": resultado.inserted_id})

    return jsonify({
        "mensagem":"Carro criado com sucesso","carro":serializar_carro(carro_criado)
    }), 201

@carros_pb.route("/carros/<id>", methods=["PUT"])
def atualizar_carro(id):
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400

    campos_atualizar = {}

    if "marca" in dados:
        campos_atualizar["marca"] = dados["marca"]
    if "modelo" in dados:
        campos_atualizar["modelo"] = dados["modelo"]
    if "ano" in dados:
        campos_atualizar["ano"] = dados["ano"]

    if not campos_atualizar:
        return jsonify({"erro": "Nenhum campo válido enviado para atualização"}), 400

    try:
        resultado = colecao.update_one(
            {"_id": ObjectId(id)},
            {"$set": campos_atualizar}
        )

        if resultado.matched_count == 0:
            return jsonify({"erro": "Carro não encontrado"}), 404

        carro_atualizado = colecao.find_one({"_id": ObjectId(id)})

        return jsonify({
            "mensagem": "Carro atualizado com sucesso",
            "carro": serializar_carro(carro_atualizado)
        }), 200

    except Exception:
        return jsonify({"erro": "ID inválido"}), 400
    
@carros_pb.route("/carros/<id>", methods=["DELETE"])
def deletar_carro(id):
    try:
        resultado = colecao.delete_one({"_id": ObjectId(id)})

        if resultado.deleted_count == 0:
            return jsonify({"erro": "Carro não encontrado"}), 404

        return jsonify({"mensagem": "Carro deletado com sucesso"}), 200

    except Exception:
        return jsonify({"erro": "ID inválido"}), 400    

# O CRUD completo cobre:
# GET /carros → lista todos
# GET /carros/<id> → busca um carro
# POST /carros → cria um carro
# PUT /carros/<id> → atualiza um carro
# DELETE /carros/<id> → remove um carro