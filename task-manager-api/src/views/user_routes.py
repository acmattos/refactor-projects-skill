from flask import Blueprint, request, jsonify
from services import user_service
from repositories import task_repository
from middlewares.auth import require_auth, generate_token

user_bp = Blueprint('users', __name__)


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all()
    result = []
    for u in users:
        data = u.to_dict()
        data['task_count'] = len(u.tasks)
        result.append(data)
    return jsonify(result), 200


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    data = user.to_dict()
    tasks = task_repository.find_by_user(user_id)
    data['tasks'] = [t.to_dict() for t in tasks]
    return jsonify(data), 200


@user_bp.route('/users/<int:user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id):
    user = user_service.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    tasks = task_repository.find_by_user(user_id)
    return jsonify([t.to_dict() for t in tasks]), 200


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    user, error = user_service.create(data)
    if error == 'EMAIL_EXISTS':
        return jsonify({'error': 'Email já cadastrado'}), 409
    if error:
        return jsonify({'error': error}), 400
    return jsonify(user.to_dict()), 201


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@require_auth
def update_user(user_id):
    user = user_service.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    updated, error = user_service.update(user, data)
    if error == 'EMAIL_EXISTS':
        return jsonify({'error': 'Email já cadastrado'}), 409
    if error:
        return jsonify({'error': error}), 400
    return jsonify(updated.to_dict()), 200


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@require_auth
def delete_user(user_id):
    user = user_service.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    ok, error = user_service.delete(user)
    if not ok:
        return jsonify({'error': error}), 500
    return jsonify({'message': 'Usuário deletado com sucesso'}), 200


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    user, error = user_service.authenticate(data.get('email'), data.get('password'))
    if error == 'INACTIVE':
        return jsonify({'error': 'Usuário inativo'}), 403
    if error:
        return jsonify({'error': error}), 401
    return jsonify({
        'message': 'Login realizado com sucesso',
        'user': user.to_dict(),
        'token': generate_token(user.id),
    }), 200
