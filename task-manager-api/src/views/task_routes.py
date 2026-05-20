from flask import Blueprint, request, jsonify
from services import task_service
from middlewares.auth import require_auth

task_bp = Blueprint('tasks', __name__)


@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = task_service.get_all()
    return jsonify([t.to_dict() for t in tasks]), 200


@task_bp.route('/tasks/stats', methods=['GET'])
def task_stats():
    return jsonify(task_service.get_stats()), 200


@task_bp.route('/tasks/search', methods=['GET'])
def search_tasks():
    query = request.args.get('q', '')
    status = request.args.get('status', '')
    priority_raw = request.args.get('priority', '')
    user_id_raw = request.args.get('user_id', '')

    priority = None
    if priority_raw:
        try:
            priority = int(priority_raw)
        except ValueError:
            return jsonify({'error': 'Prioridade deve ser um número inteiro'}), 400

    user_id = None
    if user_id_raw:
        try:
            user_id = int(user_id_raw)
        except ValueError:
            return jsonify({'error': 'user_id deve ser um número inteiro'}), 400

    tasks = task_service.search(query, status, priority, user_id)
    return jsonify([t.to_dict() for t in tasks]), 200


@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_service.get_by_id(task_id)
    if not task:
        return jsonify({'error': 'Task não encontrada'}), 404
    return jsonify(task.to_dict()), 200


@task_bp.route('/tasks', methods=['POST'])
@require_auth
def create_task():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    task, error = task_service.create(data)
    if error:
        if error in ('Usuário não encontrado', 'Categoria não encontrada'):
            return jsonify({'error': error}), 404
        return jsonify({'error': error}), 400
    return jsonify(task.to_dict()), 201


@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@require_auth
def update_task(task_id):
    task = task_service.get_by_id(task_id)
    if not task:
        return jsonify({'error': 'Task não encontrada'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    updated, error = task_service.update(task, data)
    if error:
        if error in ('Usuário não encontrado', 'Categoria não encontrada'):
            return jsonify({'error': error}), 404
        return jsonify({'error': error}), 400
    return jsonify(updated.to_dict()), 200


@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@require_auth
def delete_task(task_id):
    task = task_service.get_by_id(task_id)
    if not task:
        return jsonify({'error': 'Task não encontrada'}), 404
    ok, error = task_service.delete(task)
    if not ok:
        return jsonify({'error': error}), 500
    return jsonify({'message': 'Task deletada com sucesso'}), 200
