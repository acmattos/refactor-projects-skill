import logging
from models.category import Category
from repositories import category_repository, task_repository

logger = logging.getLogger(__name__)


def get_all():
    categories = category_repository.find_all()
    result = []
    for c in categories:
        data = c.to_dict()
        data['task_count'] = task_repository.count_by_category(c.id)
        result.append(data)
    return result


def get_by_id(cat_id):
    return category_repository.find_by_id(cat_id)


def create(data):
    name = data.get('name')
    if not name:
        return None, 'Nome é obrigatório'

    category = Category()
    category.name = name
    category.description = data.get('description', '')
    category.color = data.get('color', '#000000')

    try:
        category_repository.save(category)
        return category, None
    except Exception as e:
        category_repository.rollback()
        logger.error(f"Erro ao criar categoria: {str(e)}")
        return None, 'Erro ao criar categoria'


def update(category, data):
    if 'name' in data:
        category.name = data['name']
    if 'description' in data:
        category.description = data['description']
    if 'color' in data:
        category.color = data['color']

    try:
        category_repository.save(category)
        return category, None
    except Exception as e:
        category_repository.rollback()
        logger.error(f"Erro ao atualizar categoria: {str(e)}")
        return None, 'Erro ao atualizar'


def delete(category):
    try:
        category_repository.delete(category)
        return True, None
    except Exception as e:
        category_repository.rollback()
        return False, 'Erro ao deletar'
