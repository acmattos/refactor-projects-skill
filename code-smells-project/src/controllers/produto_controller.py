import logging
from flask import request, jsonify
from middlewares.error_handler import NotFoundError, ValidationError
import repositories.produto_repository as produto_repository
from models.produto_model import Produto

logger = logging.getLogger(__name__)


def listar_produtos():
    produtos = produto_repository.find_all()
    logger.info("Listando %s produtos", len(produtos))
    return jsonify({"dados": [p.to_dict() for p in produtos], "sucesso": True}), 200


def buscar_produto(id):
    produto = produto_repository.find_by_id(id)
    if not produto:
        raise NotFoundError("Produto não encontrado")
    return jsonify({"dados": produto.to_dict(), "sucesso": True}), 200


def buscar_produtos():
    termo = request.args.get("q", "")
    categoria = request.args.get("categoria", None)
    preco_min_raw = request.args.get("preco_min", None)
    preco_max_raw = request.args.get("preco_max", None)
    try:
        preco_min = float(preco_min_raw) if preco_min_raw else None
        preco_max = float(preco_max_raw) if preco_max_raw else None
    except ValueError:
        raise ValidationError("preco_min e preco_max devem ser numéricos")
    resultados = produto_repository.search(termo, categoria, preco_min, preco_max)
    return jsonify({"dados": [p.to_dict() for p in resultados], "total": len(resultados), "sucesso": True}), 200


def criar_produto():
    dados = request.get_json()
    try:
        Produto.validar(dados)
    except ValueError as e:
        raise ValidationError(str(e))
    id = produto_repository.create(
        dados["nome"], dados.get("descricao", ""), dados["preco"],
        dados["estoque"], dados.get("categoria", "geral"),
    )
    logger.info("Produto criado com ID: %s", id)
    return jsonify({"dados": {"id": id}, "sucesso": True, "mensagem": "Produto criado"}), 201


def atualizar_produto(id):
    produto = produto_repository.find_by_id(id)
    if not produto:
        raise NotFoundError("Produto não encontrado")
    dados = request.get_json()
    try:
        Produto.validar(dados)
    except ValueError as e:
        raise ValidationError(str(e))
    produto_repository.update(
        id, dados["nome"], dados.get("descricao", ""), dados["preco"],
        dados["estoque"], dados.get("categoria", "geral"),
    )
    return jsonify({"sucesso": True, "mensagem": "Produto atualizado"}), 200


def deletar_produto(id):
    produto = produto_repository.find_by_id(id)
    if not produto:
        raise NotFoundError("Produto não encontrado")
    produto_repository.delete(id)
    logger.info("Produto %s deletado", id)
    return jsonify({"sucesso": True, "mensagem": "Produto deletado"}), 200
