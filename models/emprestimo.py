# CLASSE EMPRÉSTIMO

class Emprestimo:
    def __init__(self, id, nome_livro, nome_aluno):
        self.id = id
        self.nome_livro = nome_livro
        self.nome_aluno = nome_aluno

    def to_dict(self):
        return {
            "id": self.id,
            "nome_livro": self.nome_livro,
            "nome_aluno": self.nome_aluno,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados.get("id", 0),
            dados["nome_livro"],
            dados["nome_aluno"],
        )

    def __str__(self):
        return (
            f'ID: {self.id}\n'
            f'Livro: {self.nome_livro}\n'
            f'Emprestado para: {self.nome_aluno}\n'
            f'{"-" * 50}'
        )