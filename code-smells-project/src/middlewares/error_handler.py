import logging
from flask import jsonify

logger = logging.getLogger(__name__)


class NotFoundError(Exception):
    pass


class ValidationError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class AuthorizationError(Exception):
    pass


def register_error_handlers(app):
    @app.errorhandler(NotFoundError)
    def handle_not_found(e):
        return jsonify({"erro": str(e), "sucesso": False}), 404

    @app.errorhandler(ValidationError)
    def handle_validation(e):
        return jsonify({"erro": str(e), "sucesso": False}), 400

    @app.errorhandler(AuthenticationError)
    def handle_authentication(e):
        return jsonify({"erro": str(e), "sucesso": False}), 401

    @app.errorhandler(AuthorizationError)
    def handle_authorization(e):
        return jsonify({"erro": str(e), "sucesso": False}), 403

    @app.errorhandler(Exception)
    def handle_generic(e):
        logger.error("Unhandled error: %s", str(e), exc_info=True)
        return jsonify({"erro": "Erro interno do servidor", "sucesso": False}), 500
