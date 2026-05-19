from werkzeug.security import generate_password_hash, check_password_hash
from infrastructure.database import get_db
from models.usuario_model import Usuario


def find_all():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, email, tipo, criado_em FROM usuarios")
    return [_row_to_usuario(row) for row in cursor.fetchall()]


def find_by_id(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, email, tipo, criado_em FROM usuarios WHERE id = ?", (id,))
    row = cursor.fetchone()
    return _row_to_usuario(row) if row else None


def authenticate(email, senha):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    row = cursor.fetchone()
    if row and check_password_hash(row["senha"], senha):
        return _row_to_usuario(row)
    return None


def create(nome, email, senha, tipo="cliente"):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (?, ?, ?, ?)",
        (nome, email, generate_password_hash(senha), tipo),
    )
    db.commit()
    return cursor.lastrowid


def count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    return cursor.fetchone()[0]


def _row_to_usuario(row):
    return Usuario(
        id=row["id"],
        nome=row["nome"],
        email=row["email"],
        tipo=row["tipo"],
        criado_em=row["criado_em"],
    )
