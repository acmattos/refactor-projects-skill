from infrastructure.database import db
from models.task import Task
from datetime import datetime, timezone


def find_all():
    return Task.query.all()


def find_by_id(task_id):
    return db.session.get(Task, task_id)


def find_by_user(user_id):
    return Task.query.filter_by(user_id=user_id).all()


def count_by_category(category_id):
    return Task.query.filter_by(category_id=category_id).count()


def search(query='', status='', priority=None, user_id=None):
    q = Task.query
    if query:
        q = q.filter(
            db.or_(
                Task.title.like(f'%{query}%'),
                Task.description.like(f'%{query}%')
            )
        )
    if status:
        q = q.filter(Task.status == status)
    if priority is not None:
        q = q.filter(Task.priority == priority)
    if user_id is not None:
        q = q.filter(Task.user_id == user_id)
    return q.all()


def count_total():
    return Task.query.count()


def count_by_status(status):
    return Task.query.filter_by(status=status).count()


def count_by_priority(priority):
    return Task.query.filter_by(priority=priority).count()


def count_recent(since):
    return Task.query.filter(Task.created_at >= since).count()


def count_done_since(since):
    return Task.query.filter(Task.status == 'done', Task.updated_at >= since).count()


def save(task):
    db.session.add(task)
    db.session.commit()


def delete(task):
    db.session.delete(task)
    db.session.commit()


def rollback():
    db.session.rollback()
