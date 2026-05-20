from flask import Blueprint, request, jsonify
from services import category_service
from middlewares.auth import require_auth

category_bp = Blueprint('categories', __name__)


@category_bp.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(category_service.get_all()), 200


@category_bp.route('/categories', methods=['POST'])
@require_auth
def create_category():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    category, error = category_service.create(data)
    if error:
        return jsonify({'error': error}), 400
    return jsonify(category.to_dict()), 201


@category_bp.route('/categories/<int:cat_id>', methods=['PUT'])
@require_auth
def update_category(cat_id):
    category = category_service.get_by_id(cat_id)
    if not category:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    updated, error = category_service.update(category, data)
    if error:
        return jsonify({'error': error}), 400
    return jsonify(updated.to_dict()), 200


@category_bp.route('/categories/<int:cat_id>', methods=['DELETE'])
@require_auth
def delete_category(cat_id):
    category = category_service.get_by_id(cat_id)
    if not category:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    ok, error = category_service.delete(category)
    if not ok:
        return jsonify({'error': error}), 500
    return jsonify({'message': 'Categoria deletada'}), 200
