class Produto:
    CATEGORIAS_VALIDAS = ["informatica", "moveis", "vestuario", "geral", "eletronicos", "livros"]

    def __init__(self, id, nome, descricao, preco, estoque, categoria, ativo=1, criado_em=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria
        self.ativo = ativo
        self.criado_em = criado_em

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque,
            "categoria": self.categoria,
            "ativo": self.ativo,
            "criado_em": self.criado_em,
        }

    @staticmethod
    def validar(dados):
        if not dados:
            raise ValueError("Dados inválidos")
        if "nome" not in dados:
            raise ValueError("Nome é obrigatório")
        if "preco" not in dados:
            raise ValueError("Preço é obrigatório")
        if "estoque" not in dados:
            raise ValueError("Estoque é obrigatório")
        nome = dados["nome"]
        preco = dados["preco"]
        estoque = dados["estoque"]
        categoria = dados.get("categoria", "geral")
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo")
        if len(nome) < 2:
            raise ValueError("Nome muito curto")
        if len(nome) > 200:
            raise ValueError("Nome muito longo")
        if categoria not in Produto.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoria inválida. Válidas: {Produto.CATEGORIAS_VALIDAS}")
