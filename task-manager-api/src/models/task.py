from infrastructure.database import db
from datetime import datetime, timezone


def _now():
    return datetime.now(timezone.utc).replace(tzinfo=None)


class Task(db.Model):
    __tablename__ = 'tasks'

    VALID_STATUSES = ['pending', 'in_progress', 'done', 'cancelled']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default='pending')
    priority = db.Column(db.Integer, default=3)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=_now)
    updated_at = db.Column(db.DateTime, default=_now, onupdate=_now)
    due_date = db.Column(db.DateTime, nullable=True)
    tags = db.Column(db.String(500), nullable=True)

    user = db.relationship('User', backref=db.backref('tasks', lazy='select'), lazy='joined')
    category = db.relationship('Category', backref=db.backref('tasks', lazy='select'), lazy='joined')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'due_date': str(self.due_date) if self.due_date else None,
            'tags': self.tags.split(',') if self.tags else [],
            'overdue': self.is_overdue(),
            'user_name': self.user.name if self.user else None,
            'category_name': self.category.name if self.category else None,
        }

    def validate_status(self, new_status):
        return new_status in self.VALID_STATUSES

    def validate_priority(self, p):
        return 1 <= p <= 5

    def is_overdue(self):
        if self.due_date:
            return self.due_date < _now() and self.status not in ('done', 'cancelled')
        return False
