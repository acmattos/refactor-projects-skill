import logging
from flask import request, jsonify
from middlewares.error_handler import NotFoundError, ValidationError, AuthenticationError
import repositories.usuario_repository as usuario_repository

logger = logging.getLogger(__name__)


def listar_usuarios():
    usuarios = usuario_repository.find_all()
    return jsonify({"dados": [u.to_dict() for u in usuarios], "sucesso": True}), 200


def buscar_usuario(id):
    usuario = usuario_repository.find_by_id(id)
    if not usuario:
        raise NotFoundError("Usuário não encontrado")
    return jsonify({"dados": usuario.to_dict(), "sucesso": True}), 200


def criar_usuario():
    dados = request.get_json()
    if not dados:
        raise ValidationError("Dados inválidos")
    nome = dados.get("nome", "")
    email = dados.get("email", "")
    senha = dados.get("senha", "")
    if not nome or not email or not senha:
        raise ValidationError("Nome, email e senha são obrigatórios")
    id = usuario_repository.create(nome, email, senha)
    logger.info("Usuário criado: %s", email)
    return jsonify({"dados": {"id": id}, "sucesso": True}), 201


def login():
    dados = request.get_json()
    if not dados:
        raise ValidationError("Dados inválidos")
    email = dados.get("email", "")
    senha = dados.get("senha", "")
    if not email or not senha:
        raise ValidationError("Email e senha são obrigatórios")
    usuario = usuario_repository.authenticate(email, senha)
    if not usuario:
        logger.warning("Login falhou: %s", email)
        raise AuthenticationError("Email ou senha inválidos")
    logger.info("Login bem-sucedido: %s", email)
    return jsonify({"dados": usuario.to_dict(), "sucesso": True, "mensagem": "Login OK"}), 200
