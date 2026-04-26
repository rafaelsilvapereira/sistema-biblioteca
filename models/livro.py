# CLASSE LIVRO

class Livro:
    def __init__(self, id, data, nome, estoque):
        self.id = id
        self.data = data
        self.nome = nome
        self.estoque = estoque
        self.emprestado = 0

    def to_dict(self):
        return {
            "id": self.id,
            "data": self.data,
            "nome": self.nome,
            "estoque": self.estoque,
            "emprestado": self.emprestado,
        }

    def emprestar(self):
        if self.quantidade <= 0:
            return False

        self.emprestado += 1
        return True

    @property
    def quantidade(self):
        return self.estoque - self.emprestado

    @property
    def status(self):
        return "Indisponível" if self.quantidade == 0 else "Disponível"

    @classmethod
    def from_dict(cls, dados):
        livro = cls(
            dados.get("id", 0),
            dados["data"],
            dados["nome"],
            dados["estoque"],
        )

        livro.emprestado = dados.get("emprestado", 0)

        return livro
    
    def __str__(self):
        return (
            f'ID: {self.id}\n'
            f'Data: {self.data}\n'
            f'Nome: {self.nome}\n'
            f'Quantidade: {self.quantidade}\n'
            f'Emprestado: {self.emprestado}\n'
            f'Status: {self.status}\n'
            f'{"-" * 50}'
        )