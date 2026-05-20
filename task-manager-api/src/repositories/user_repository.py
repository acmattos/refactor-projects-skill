from infrastructure.database import db
from models.user import User
from sqlalchemy.orm import selectinload


def find_all_with_tasks():
    return User.query.options(selectinload(User.tasks)).all()


def find_by_id(user_id):
    return db.session.get(User, user_id)


def find_by_id_with_tasks(user_id):
    return User.query.options(selectinload(User.tasks)).filter_by(id=user_id).first()


def find_by_email(email):
    return User.query.filter_by(email=email).first()


def save(user):
    db.session.add(user)
    db.session.commit()


def delete_with_tasks(user):
    from models.task import Task
    Task.query.filter_by(user_id=user.id).delete()
    db.session.delete(user)
    db.session.commit()


def rollback():
    db.session.rollback()
