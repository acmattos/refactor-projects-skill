from infrastructure.database import db
from models.category import Category


def find_all():
    return Category.query.all()


def find_by_id(cat_id):
    return db.session.get(Category, cat_id)


def save(category):
    db.session.add(category)
    db.session.commit()


def delete(category):
    db.session.delete(category)
    db.session.commit()


def rollback():
    db.session.rollback()
