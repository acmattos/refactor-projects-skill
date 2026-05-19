from infrastructure.database import get_db
from models.pedido_model import Pedido


def find_by_usuario(usuario_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT p.id, p.usuario_id, p.status, p.total, p.criado_em,
               ip.produto_id, ip.quantidade, ip.preco_unitario, pr.nome AS produto_nome
        FROM pedidos p
        LEFT JOIN itens_pedido ip ON ip.pedido_id = p.id
        LEFT JOIN produtos pr ON pr.id = ip.produto_id
        WHERE p.usuario_id = ?
        ORDER BY p.id
        """,
        (usuario_id,),
    )
    return _rows_to_pedidos(cursor.fetchall())


def find_all():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT p.id, p.usuario_id, p.status, p.total, p.criado_em,
               ip.produto_id, ip.quantidade, ip.preco_unitario, pr.nome AS produto_nome
        FROM pedidos p
        LEFT JOIN itens_pedido ip ON ip.pedido_id = p.id
        LEFT JOIN produtos pr ON pr.id = ip.produto_id
        ORDER BY p.id
        """
    )
    return _rows_to_pedidos(cursor.fetchall())


def create_with_items(usuario_id, total, items):
    """items: list of (produto_id, quantidade, preco_unitario)"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO pedidos (usuario_id, status, total) VALUES (?, 'pendente', ?)",
        (usuario_id, total),
    )
    pedido_id = cursor.lastrowid
    for produto_id, quantidade, preco_unitario in items:
        cursor.execute(
            "INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
            (pedido_id, produto_id, quantidade, preco_unitario),
        )
        cursor.execute(
            "UPDATE produtos SET estoque = estoque - ? WHERE id = ?",
            (quantidade, produto_id),
        )
    db.commit()
    return pedido_id


def update_status(pedido_id, novo_status):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE pedidos SET status = ? WHERE id = ?",
        (novo_status, pedido_id),
    )
    db.commit()


def get_stats():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedidos")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(total) FROM pedidos")
    faturamento = cursor.fetchone()[0] or 0
    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status = 'pendente'")
    pendentes = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status = 'aprovado'")
    aprovados = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status = 'cancelado'")
    cancelados = cursor.fetchone()[0]
    return {
        "total": total,
        "faturamento": faturamento,
        "pendentes": pendentes,
        "aprovados": aprovados,
        "cancelados": cancelados,
    }


def count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedidos")
    return cursor.fetchone()[0]


def _rows_to_pedidos(rows):
    pedidos = {}
    for row in rows:
        pid = row["id"]
        if pid not in pedidos:
            pedidos[pid] = Pedido(
                id=row["id"],
                usuario_id=row["usuario_id"],
                status=row["status"],
                total=row["total"],
                criado_em=row["criado_em"],
                itens=[],
            )
        if row["produto_id"] is not None:
            pedidos[pid].itens.append(
                {
                    "produto_id": row["produto_id"],
                    "produto_nome": row["produto_nome"] or "Desconhecido",
                    "quantidade": row["quantidade"],
                    "preco_unitario": row["preco_unitario"],
                }
            )
    return list(pedidos.values())
