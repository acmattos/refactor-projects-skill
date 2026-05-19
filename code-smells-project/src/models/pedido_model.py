STATUSES_VALIDOS = ["pendente", "aprovado", "enviado", "entregue", "cancelado"]


class Pedido:
    def __init__(self, id, usuario_id, status, total, criado_em=None, itens=None):
        self.id = id
        self.usuario_id = usuario_id
        self.status = status
        self.total = total
        self.criado_em = criado_em
        self.itens = itens or []

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "status": self.status,
            "total": self.total,
            "criado_em": self.criado_em,
            "itens": self.itens,
        }
