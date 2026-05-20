import logging
from models.user import User
from repositories import user_repository
from utils.validators import validate_email

logger = logging.getLogger(__name__)

VALID_ROLES = ['user', 'admin', 'manager']
MIN_PASSWORD_LENGTH = 4


def get_all():
    return user_repository.find_all_with_tasks()


def get_by_id(user_id):
    return user_repository.find_by_id(user_id)


def create(data):
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')

    if not name:
        return None, 'Nome é obrigatório'
    if not email:
        return None, 'Email é obrigatório'
    if not password:
        return None, 'Senha é obrigatória'
    if not validate_email(email):
        return None, 'Email inválido'
    if len(password) < MIN_PASSWORD_LENGTH:
        return None, f'Senha deve ter no mínimo {MIN_PASSWORD_LENGTH} caracteres'
    if role not in VALID_ROLES:
        return None, 'Role inválido'
    if user_repository.find_by_email(email):
        return None, 'EMAIL_EXISTS'

    user = User()
    user.name = name
    user.email = email
    user.set_password(password)
    user.role = role

    try:
        user_repository.save(user)
        logger.info(f"Usuário criado: {user.id} - {user.name}")
        return user, None
    except Exception as e:
        user_repository.rollback()
        logger.error(f"Erro ao criar usuário: {str(e)}")
        return None, 'Erro ao criar usuário'


def update(user, data):
    if 'name' in data:
        user.name = data['name']

    if 'email' in data:
        if not validate_email(data['email']):
            return None, 'Email inválido'
        existing = user_repository.find_by_email(data['email'])
        if existing and existing.id != user.id:
            return None, 'EMAIL_EXISTS'
        user.email = data['email']

    if 'password' in data:
        if len(data['password']) < MIN_PASSWORD_LENGTH:
            return None, 'Senha muito curta'
        user.set_password(data['password'])

    if 'role' in data:
        if data['role'] not in VALID_ROLES:
            return None, 'Role inválido'
        user.role = data['role']

    if 'active' in data:
        user.active = data['active']

    try:
        user_repository.save(user)
        return user, None
    except Exception as e:
        user_repository.rollback()
        logger.error(f"Erro ao atualizar usuário: {str(e)}")
        return None, 'Erro ao atualizar'


def delete(user):
    try:
        user_repository.delete_with_tasks(user)
        logger.info(f"Usuário deletado: {user.id}")
        return True, None
    except Exception as e:
        user_repository.rollback()
        return False, 'Erro ao deletar'


def authenticate(email, password):
    if not email or not password:
        return None, 'Email e senha são obrigatórios'
    user = user_repository.find_by_email(email)
    if not user or not user.check_password(password):
        return None, 'Credenciais inválidas'
    if not user.active:
        return None, 'INACTIVE'
    return user, None
