import json

from config import ARQUIVO_EMPRESTIMOS, garantir_arquivo_json
from config import ARQUIVO_LIVROS

import utils.utils as u
import models.emprestimo as me
import models.livro as ml

# EMPRESTAR LIVRO

def emprestar_livro(sistema):
    u.titulo_menu('EMPRESTAR LIVRO')

    nome_livro = u.input_texto('\nNome do Livro: ')

    livros_encontrados = sistema.buscar_por_nome(sistema.livros, nome_livro)

    if len(livros_encontrados) == 0:
        u.mensagem_de_informacao(f'ATENÇÃO! Livro não localizado/cadastrado.', "AMARELO", "-")
        u.pausar()
        return

    else:
        u.titulo_menu(f'RESULTADO DA BUSCA POR "{nome_livro}":')

        for livro in livros_encontrados:
            print(f'\n{livro}')

        id_livro = u.input_inteiro('\nDigite o ID do Livro: ')

        obj_livro = sistema.buscar_por_id(sistema.livros, id_livro)

        if obj_livro:
            if obj_livro.status == "Indisponível":
                u.mensagem_de_informacao(f'ATENÇÃO! O livro não está disponível para empréstimo', "AMARELO", "-")
                u.pausar()
                return
            
            nome_aluno = u.input_texto('\nNome do Aluno: ')

            alunos_encontrados = sistema.buscar_por_nome(sistema.alunos, nome_aluno)

            if len(alunos_encontrados) == 0:
                u.mensagem_de_informacao(f'ATENÇÃO! Aluno não localizado/cadastrado.', "AMARELO", "-")
                u.pausar()
                return

            else:
                u.titulo_menu(f'RESULTADO DA BUSCA POR "{nome_aluno}":')

                for aluno in alunos_encontrados:
                    print(f'\n{aluno}')
                
                id_aluno = u.input_inteiro('\nDigite o ID do Aluno: ')

                obj_aluno = sistema.buscar_por_id(sistema.alunos, id_aluno)

                if obj_aluno:
                    id = sistema.gerar_id_emprestimo()

                    emprestimo = me.Emprestimo(id, obj_livro.nome, obj_aluno.nome)

                    obj_livro.quantidade -= 1
                    obj_livro.atualizar_status()
                    sistema.salvar_json(sistema.livros, ARQUIVO_LIVROS)

                    sistema.adicionar_emprestimo(emprestimo)
                    sistema.salvar_json(sistema.emprestimos, ARQUIVO_EMPRESTIMOS)

                    u.mensagem_de_informacao(f'SUCESSO! O livro "{obj_livro.nome}" foi emprestado para o aluno "{obj_aluno.nome}"!', "VERDE", '-')
                    u.pausar()

                else:
                    u.mensagem_de_informacao('ERRO! O ID do aluno não foi localizado!', "VERMELHO", "x")
                    u.pausar()
                    return

        else:
            u.mensagem_de_informacao('ERRO! O ID do livro não foi localizado!', "VERMELHO", "x")
            u.pausar()
            return

# LISTAR LIVROS EMPRESTADOS

def listar_livros_emprestados(sistema):
    u.titulo_menu('LIVROS EMPRESTADOS:')

    for livro in sistema.emprestimos:
        print(f'\n{livro}')

    u.pausar()

# CARREGAR LIVROS EMPRESTADOS JSON

def carregar_json_emprestimos():
    garantir_arquivo_json(ARQUIVO_EMPRESTIMOS)

    try:
        with open(ARQUIVO_EMPRESTIMOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            return [me.Emprestimo.from_dict(d) for d in dados]

    except FileNotFoundError:
        return []