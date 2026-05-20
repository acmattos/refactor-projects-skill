from flask import Blueprint, jsonify
from services import report_service
from repositories import user_repository

report_bp = Blueprint('reports', __name__)


@report_bp.route('/reports/summary', methods=['GET'])
def summary_report():
    return jsonify(report_service.summary()), 200


@report_bp.route('/reports/user/<int:user_id>', methods=['GET'])
def user_report_view(user_id):
    user = user_repository.find_by_id_with_tasks(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    return jsonify(report_service.user_report(user)), 200
