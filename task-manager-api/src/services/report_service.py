from datetime import datetime, timezone, timedelta
from repositories import task_repository, user_repository, category_repository
from sqlalchemy.orm import selectinload
from models.user import User


def _now():
    return datetime.now(timezone.utc).replace(tzinfo=None)


def summary():
    total_tasks = task_repository.count_total()
    all_tasks = task_repository.find_all()
    done = task_repository.count_by_status('done')

    overdue_list = []
    for t in all_tasks:
        if t.is_overdue():
            overdue_list.append({
                'id': t.id,
                'title': t.title,
                'due_date': str(t.due_date),
                'days_overdue': (_now() - t.due_date).days,
            })

    seven_days_ago = _now() - timedelta(days=7)

    from infrastructure.database import db
    users = User.query.options(selectinload(User.tasks)).all()
    user_stats = []
    for u in users:
        total = len(u.tasks)
        completed = sum(1 for t in u.tasks if t.status == 'done')
        user_stats.append({
            'user_id': u.id,
            'user_name': u.name,
            'total_tasks': total,
            'completed_tasks': completed,
            'completion_rate': round((completed / total) * 100, 2) if total > 0 else 0,
        })

    return {
        'generated_at': str(_now()),
        'overview': {
            'total_tasks': total_tasks,
            'total_users': len(users),
            'total_categories': len(category_repository.find_all()),
        },
        'tasks_by_status': {
            'pending': task_repository.count_by_status('pending'),
            'in_progress': task_repository.count_by_status('in_progress'),
            'done': done,
            'cancelled': task_repository.count_by_status('cancelled'),
        },
        'tasks_by_priority': {
            'critical': task_repository.count_by_priority(1),
            'high': task_repository.count_by_priority(2),
            'medium': task_repository.count_by_priority(3),
            'low': task_repository.count_by_priority(4),
            'minimal': task_repository.count_by_priority(5),
        },
        'overdue': {
            'count': len(overdue_list),
            'tasks': overdue_list,
        },
        'recent_activity': {
            'tasks_created_last_7_days': task_repository.count_recent(seven_days_ago),
            'tasks_completed_last_7_days': task_repository.count_done_since(seven_days_ago),
        },
        'user_productivity': user_stats,
    }


def user_report(user):
    tasks = user.tasks
    total = len(tasks)
    done = pending = in_progress = cancelled = overdue = high_priority = 0

    for t in tasks:
        if t.status == 'done':
            done += 1
        elif t.status == 'pending':
            pending += 1
        elif t.status == 'in_progress':
            in_progress += 1
        elif t.status == 'cancelled':
            cancelled += 1
        if t.priority <= 2:
            high_priority += 1
        if t.is_overdue():
            overdue += 1

    return {
        'user': {'id': user.id, 'name': user.name, 'email': user.email},
        'statistics': {
            'total_tasks': total,
            'done': done,
            'pending': pending,
            'in_progress': in_progress,
            'cancelled': cancelled,
            'overdue': overdue,
            'high_priority': high_priority,
            'completion_rate': round((done / total) * 100, 2) if total > 0 else 0,
        },
    }
