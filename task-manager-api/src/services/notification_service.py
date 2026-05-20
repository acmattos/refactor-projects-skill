import smtplib
import logging
from config import settings

logger = logging.getLogger(__name__)


class NotificationService:
    def __init__(self):
        self.email_host = 'smtp.gmail.com'
        self.email_port = 587
        self.email_user = settings.EMAIL_USER
        self.email_password = settings.EMAIL_PASSWORD

    def send_email(self, to, subject, body):
        try:
            server = smtplib.SMTP(self.email_host, self.email_port)
            server.starttls()
            server.login(self.email_user, self.email_password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(self.email_user, to, message)
            server.quit()
            logger.info(f"Email enviado para {to}")
            return True
        except Exception as e:
            logger.error(f"Erro ao enviar email: {str(e)}")
            return False

    def notify_task_assigned(self, user, task):
        subject = f"Nova task atribuída: {task.title}"
        body = (
            f"Olá {user.name},\n\n"
            f"A task '{task.title}' foi atribuída a você.\n\n"
            f"Prioridade: {task.priority}\nStatus: {task.status}"
        )
        self.send_email(user.email, subject, body)

    def notify_task_overdue(self, user, task):
        # Pendente: requer job agendado (ex: Celery beat ou cron) para disparar
        # periodicamente. Operador deve configurar scheduler que chame este método
        # para tasks com due_date vencida e status não concluído.
        subject = f"Task atrasada: {task.title}"
        body = (
            f"Olá {user.name},\n\n"
            f"A task '{task.title}' está atrasada!\n\n"
            f"Data limite: {task.due_date}"
        )
        self.send_email(user.email, subject, body)
