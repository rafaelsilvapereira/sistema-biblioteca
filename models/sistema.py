import json

# CLASSE SISTEMA - Controle (Sem Inputs)

class SistemaBiblioteca:
    # Variáveis de Armazenamento e Controle
    def __init__(self):
        self.alunos = []
        self.livros = []
        self.ultimo_id_aluno = 0
        self.ultimo_id_livro = 0
        
    # --------------------------------------------------
    # FUNÇÕES CLASSE ALUNO
    # --------------------------------------------------

    def gerar_id_aluno(self):
        self.ultimo_id_aluno += 1
        return self.ultimo_id_aluno
    
    def carregar_ids_aluno(self):
        if self.alunos:
            self.ultimo_id_aluno = max(aluno.id for aluno in self.alunos)

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def remover_aluno(self, aluno):
        self.alunos.remove(aluno)

    # # Busca Retorna Todos os Encontrados Com o Termo Pesquisado
    # def buscar_aluno_nome(self, nome):
    #     encontrados = []

    #     for aluno in self.alunos:
    #         if nome.lower() in aluno.nome.lower():
    #             encontrados.append(aluno)
    #     return encontrados
    
    # def buscar_aluno_por_id(self, id_aluno):
    #     for aluno in self.alunos:
    #         if aluno.id == id_aluno:
    #             return aluno
    #     return None

    # SALVAR JSON - Atualizada (Qualquer Pasta)

    def salvar_json(self, lista_objetos, caminho_arquivo):
        try:
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                json.dump([obj.to_dict() for obj in lista_objetos], f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar alunos: {e}")

    # --------------------------------------------------
    # FUNÇÕES CLASSE LIVRO
    # --------------------------------------------------

    def gerar_id_livro(self):
        self.ultimo_id_livro += 1
        return self.ultimo_id_livro

    def carregar_ids_livro(self):
        if self.livros:
            self.ultimo_id_livro = max(livro.id for livro in self.livros)

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    # def buscar_livro_nome(self, nome):
    #     encontrados = []

    #     for livro in self.livros:
    #         if nome.lower() in livro.nome.lower():
    #             encontrados.append(livro)
    #     return encontrados

    # def buscar_livro_por_id(self, id_livro):
    #     for livro in self.livros:
    #         if livro.id == id_livro:
    #             return livro
    #     return None

    # --------------------------------------------------
    # FUNÇÕES GENÉRICAS
    # --------------------------------------------------

    # BUSCAR POR NOME

    def buscar_por_nome(self, lista_objetos, nome):
        return [obj for obj in lista_objetos if nome.lower() in obj.nome.lower()]
    
    # BUSCAR POR ID

    def buscar_por_id(self, lista_objetos, id):
        for obj in lista_objetos:
            if obj.id == id:
                return obj
        return None

    # SALVAR JSON (Qualquer Pasta)

    def salvar_json(self, lista_objetos, caminho_arquivo):
        try:
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                json.dump([obj.to_dict() for obj in lista_objetos], f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar alunos: {e}")