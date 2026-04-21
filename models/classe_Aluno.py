# CLASSE ALUNO - Modelo

class Aluno:
    def __init__(self, id, nome, celular, email):
        self.id = id
        self.nome = nome
        self.celular = str(celular)
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "celular": self.celular,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados.get("id", 0),
            dados["nome"],
            str(dados["celular"]),
            dados["email"]
        )

    def __str__(self):
        return (
            f'ID: {self.id}\n'
            f'Nome: {self.nome}\n'
            f'Celular: {self.celular}\n'
            f'Email: {self.email}\n'
            f'{"-" * 50}'
        )