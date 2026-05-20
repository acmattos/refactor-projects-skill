import os
import sys
import datetime

# Garante que src/ está no path para execução direta: python src/app.py
_SRC = os.path.dirname(os.path.abspath(__file__))
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

from flask import Flask
from flask_cors import CORS
from config import settings
from infrastructure.database import db, init_db
from views.task_routes import task_bp
from views.user_routes import user_bp
from views.category_routes import category_bp
from views.report_routes import report_bp
from middlewares.error_handler import register_error_handlers

_PROJECT_ROOT = os.path.dirname(_SRC)
_INSTANCE_DIR = os.path.join(_PROJECT_ROOT, 'instance')
os.makedirs(_INSTANCE_DIR, exist_ok=True)


def create_app():
    app = Flask(__name__, instance_path=_INSTANCE_DIR)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = settings.SECRET_KEY

    CORS(app)
    init_db(app)

    app.register_blueprint(task_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(report_bp)

    register_error_handlers(app)

    @app.route('/health')
    def health():
        return {'status': 'ok', 'timestamp': str(datetime.datetime.now(datetime.timezone.utc))}

    @app.route('/')
    def index():
        return {'message': 'Task Manager API', 'version': '1.0'}

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
