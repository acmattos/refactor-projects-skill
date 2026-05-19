import os
import sys
import logging

# Resolve absolute DB path before any config import
_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DATABASE_URL", os.path.join(_root, "loja.db"))

from flask import Flask, jsonify
from flask_cors import CORS

from config import settings
from infrastructure.database import init_db
from infrastructure.seed import run_seed
from views.routes import register_routes
from middlewares.error_handler import register_error_handlers

logging.basicConfig(level=logging.INFO)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["DEBUG"] = settings.DEBUG
    CORS(app)
    init_db(app)
    with app.app_context():
        run_seed()
    register_error_handlers(app)
    register_routes(app)

    @app.route("/")
    def index():
        return jsonify({
            "mensagem": "Bem-vindo à API da Loja",
            "versao": "1.0.0",
            "endpoints": {
                "produtos": "/produtos",
                "usuarios": "/usuarios",
                "pedidos": "/pedidos",
                "login": "/login",
                "relatorios": "/relatorios/vendas",
                "health": "/health",
            },
        })

    return app


app = create_app()


def main():
    logger = logging.getLogger(__name__)
    logger.info("=" * 50)
    logger.info("SERVIDOR INICIADO")
    logger.info("Rodando em http://localhost:5000")
    logger.info("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=settings.DEBUG)


if __name__ == "__main__":
    main()
