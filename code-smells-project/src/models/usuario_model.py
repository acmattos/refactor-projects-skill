class Usuario:
    def __init__(self, id, nome, email, tipo, criado_em=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo = tipo
        self.criado_em = criado_em

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "tipo": self.tipo,
            "criado_em": self.criado_em,
        }
