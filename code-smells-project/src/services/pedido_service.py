import logging
import repositories.produto_repository as produto_repository
import repositories.pedido_repository as pedido_repository

logger = logging.getLogger(__name__)


def criar_pedido(usuario_id, itens):
    total = 0
    items_to_create = []

    for item in itens:
        produto = produto_repository.find_by_id(item["produto_id"])
        if produto is None:
            raise ValueError(f"Produto {item['produto_id']} não encontrado")
        if produto.estoque < item["quantidade"]:
            raise ValueError(f"Estoque insuficiente para {produto.nome}")
        total += produto.preco * item["quantidade"]
        items_to_create.append((item["produto_id"], item["quantidade"], produto.preco))

    pedido_id = pedido_repository.create_with_items(usuario_id, total, items_to_create)
    logger.info("Pedido %s criado para usuario %s", pedido_id, usuario_id)
    return {"pedido_id": pedido_id, "total": total}
