# CLASSE LIVRO

class Livro:
    def __init__(self, id, data, nome, quantidade):
        self.id = id
        self.data = data
        self.nome = nome
        self.quantidade = quantidade
        self.status = None
        self.atualizar_status()

    def to_dict(self):
        return {
            "id": self.id,
            "data": self.data,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "status": self.status
        }
    
    def atualizar_status(self):
        self.status = "Indisponível" if self.quantidade == 0 else "Disponível"
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados.get("id", 0),
            dados["data"],
            dados["nome"],
            dados["quantidade"],
        )
    
    def __str__(self):
        return (
            f'ID: {self.id}\n'
            f'Data: {self.data}\n'
            f'Nome: {self.nome}\n'
            f'Quantidade: {self.quantidade}\n'
            f'Status: {self.status}\n'
            f'{"-" * 50}'
        )