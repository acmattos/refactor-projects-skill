import logging
from flask import request, jsonify
from middlewares.error_handler import ValidationError
import repositories.pedido_repository as pedido_repository
import services.pedido_service as pedido_service
import services.relatorio_service as relatorio_service
from models.pedido_model import STATUSES_VALIDOS

logger = logging.getLogger(__name__)


def criar_pedido():
    dados = request.get_json()
    if not dados:
        raise ValidationError("Dados inválidos")
    usuario_id = dados.get("usuario_id")
    itens = dados.get("itens", [])
    if not usuario_id:
        raise ValidationError("Usuario ID é obrigatório")
    if not itens:
        raise ValidationError("Pedido deve ter pelo menos 1 item")
    try:
        resultado = pedido_service.criar_pedido(usuario_id, itens)
    except ValueError as e:
        raise ValidationError(str(e))
    return jsonify({"dados": resultado, "sucesso": True, "mensagem": "Pedido criado com sucesso"}), 201


def listar_todos_pedidos():
    pedidos = pedido_repository.find_all()
    return jsonify({"dados": [p.to_dict() for p in pedidos], "sucesso": True}), 200


def listar_pedidos_usuario(usuario_id):
    pedidos = pedido_repository.find_by_usuario(usuario_id)
    return jsonify({"dados": [p.to_dict() for p in pedidos], "sucesso": True}), 200


def atualizar_status_pedido(pedido_id):
    dados = request.get_json()
    novo_status = dados.get("status", "")
    if novo_status not in STATUSES_VALIDOS:
        raise ValidationError("Status inválido")
    pedido_repository.update_status(pedido_id, novo_status)
    if novo_status == "aprovado":
        logger.info("Pedido %s aprovado. Preparar envio.", pedido_id)
    if novo_status == "cancelado":
        logger.info("Pedido %s cancelado. Devolver estoque.", pedido_id)
    return jsonify({"sucesso": True, "mensagem": "Status atualizado"}), 200


def relatorio_vendas():
    relatorio = relatorio_service.relatorio_vendas()
    return jsonify({"dados": relatorio, "sucesso": True}), 200
