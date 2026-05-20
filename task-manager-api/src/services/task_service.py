import logging
from models.task import Task
from repositories import task_repository, user_repository, category_repository
from services.notification_service import NotificationService
from utils.date_utils import parse_date

logger = logging.getLogger(__name__)
_notifier = NotificationService()


def get_all():
    return task_repository.find_all()


def get_by_id(task_id):
    return task_repository.find_by_id(task_id)


def create(data):
    title = (data.get('title') or '').strip()
    if not title:
        return None, 'Título é obrigatório'
    if len(title) < 3:
        return None, 'Título muito curto'
    if len(title) > 200:
        return None, 'Título muito longo'

    status = data.get('status', 'pending')
    priority = data.get('priority', 3)
    user_id = data.get('user_id')
    category_id = data.get('category_id')

    task = Task()
    if not task.validate_status(status):
        return None, 'Status inválido'
    if not task.validate_priority(priority):
        return None, 'Prioridade deve ser entre 1 e 5'

    if user_id:
        if not user_repository.find_by_id(user_id):
            return None, 'Usuário não encontrado'
    if category_id:
        if not category_repository.find_by_id(category_id):
            return None, 'Categoria não encontrada'

    task.title = title
    task.description = data.get('description', '')
    task.status = status
    task.priority = priority
    task.user_id = user_id
    task.category_id = category_id

    due_date_raw = data.get('due_date')
    if due_date_raw:
        parsed = parse_date(due_date_raw)
        if not parsed:
            return None, 'Formato de data inválido. Use YYYY-MM-DD'
        task.due_date = parsed

    tags = data.get('tags')
    if tags:
        task.tags = ','.join(tags) if isinstance(tags, list) else tags

    try:
        task_repository.save(task)
        logger.info(f"Task criada: {task.id} - {task.title}")
        if user_id:
            try:
                user = user_repository.find_by_id(user_id)
                if user:
                    _notifier.notify_task_assigned(user, task)
            except Exception as e:
                logger.error(f"Falha ao enviar notificação de atribuição: {e}")
        return task, None
    except Exception as e:
        task_repository.rollback()
        logger.error(f"Erro ao criar task: {str(e)}")
        return None, 'Erro ao criar task'


def update(task, data):
    if 'title' in data:
        title = data['title']
        if len(title) < 3:
            return None, 'Título muito curto'
        if len(title) > 200:
            return None, 'Título muito longo'
        task.title = title

    if 'description' in data:
        task.description = data['description']

    if 'status' in data:
        if not task.validate_status(data['status']):
            return None, 'Status inválido'
        task.status = data['status']

    if 'priority' in data:
        if not task.validate_priority(data['priority']):
            return None, 'Prioridade deve ser entre 1 e 5'
        task.priority = data['priority']

    if 'user_id' in data:
        if data['user_id'] and not user_repository.find_by_id(data['user_id']):
            return None, 'Usuário não encontrado'
        task.user_id = data['user_id']

    if 'category_id' in data:
        if data['category_id'] and not category_repository.find_by_id(data['category_id']):
            return None, 'Categoria não encontrada'
        task.category_id = data['category_id']

    if 'due_date' in data:
        if data['due_date']:
            parsed = parse_date(data['due_date'])
            if not parsed:
                return None, 'Formato de data inválido'
            task.due_date = parsed
        else:
            task.due_date = None

    if 'tags' in data:
        task.tags = ','.join(data['tags']) if isinstance(data['tags'], list) else data['tags']

    try:
        task_repository.save(task)
        logger.info(f"Task atualizada: {task.id}")
        return task, None
    except Exception as e:
        task_repository.rollback()
        logger.error(f"Erro ao atualizar task: {str(e)}")
        return None, 'Erro ao atualizar'


def delete(task):
    try:
        task_repository.delete(task)
        logger.info(f"Task deletada: {task.id}")
        return True, None
    except Exception as e:
        task_repository.rollback()
        return False, 'Erro ao deletar'


def search(query='', status='', priority=None, user_id=None):
    return task_repository.search(query, status, priority, user_id)


def get_stats():
    total = task_repository.count_total()
    all_tasks = task_repository.find_all()
    done = task_repository.count_by_status('done')
    overdue_count = sum(1 for t in all_tasks if t.is_overdue())
    return {
        'total': total,
        'pending': task_repository.count_by_status('pending'),
        'in_progress': task_repository.count_by_status('in_progress'),
        'done': done,
        'cancelled': task_repository.count_by_status('cancelled'),
        'overdue': overdue_count,
        'completion_rate': round((done / total) * 100, 2) if total > 0 else 0,
    }
