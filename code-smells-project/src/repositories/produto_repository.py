from infrastructure.database import get_db
from models.produto_model import Produto


def find_all():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos")
    return [_row_to_produto(row) for row in cursor.fetchall()]


def find_by_id(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    row = cursor.fetchone()
    return _row_to_produto(row) if row else None


def search(termo, categoria=None, preco_min=None, preco_max=None):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM produtos WHERE 1=1"
    params = []
    if termo:
        query += " AND (nome LIKE ? OR descricao LIKE ?)"
        params.extend([f"%{termo}%", f"%{termo}%"])
    if categoria:
        query += " AND categoria = ?"
        params.append(categoria)
    if preco_min is not None:
        query += " AND preco >= ?"
        params.append(preco_min)
    if preco_max is not None:
        query += " AND preco <= ?"
        params.append(preco_max)
    cursor.execute(query, params)
    return [_row_to_produto(row) for row in cursor.fetchall()]


def create(nome, descricao, preco, estoque, categoria):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao, preco, estoque, categoria) VALUES (?, ?, ?, ?, ?)",
        (nome, descricao, preco, estoque, categoria),
    )
    db.commit()
    return cursor.lastrowid


def update(id, nome, descricao, preco, estoque, categoria):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = ?, descricao = ?, preco = ?, estoque = ?, categoria = ? WHERE id = ?",
        (nome, descricao, preco, estoque, categoria, id),
    )
    db.commit()


def delete(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    db.commit()


def count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM produtos")
    return cursor.fetchone()[0]


def _row_to_produto(row):
    return Produto(
        id=row["id"],
        nome=row["nome"],
        descricao=row["descricao"],
        preco=row["preco"],
        estoque=row["estoque"],
        categoria=row["categoria"],
        ativo=row["ativo"],
        criado_em=row["criado_em"],
    )
