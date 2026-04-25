import json

from config import ARQUIVO_ALUNOS, garantir_arquivo_json

import utils.menus as menus
import utils.utils as u
import models.aluno as ma

# CADASTRAR ALUNO

def cadastrar_aluno(sistema):
    u.titulo_menu('CADASTRAR ALUNO')

    nome = u.input_texto('\nNome do Aluno: ')

    if u.algo_ja_cadastrado(nome, sistema.alunos, "Aluno"): return

    celular = u.input_celular('\nCelular (Máx. 11 dígitos): ')

    email = u.input_texto('\nE-Mail: ')

    id = sistema.gerar_id_aluno()

    aluno = ma.Aluno(id, nome, celular, email)

    sistema.adicionar_aluno(aluno)

    sistema.salvar_json(sistema.alunos, ARQUIVO_ALUNOS)

    u.mensagem_de_informacao(f'SUCESSO! O Aluno "{nome}" foi cadastrado!', "VERDE", "-")
    
    u.pausar()

# LISTAR ALUNOS

def listar_alunos(sistema):
    u.titulo_menu('ALUNOS CADASTRADOS:')

    for aluno in sistema.alunos:
        print(f'\n{aluno}')

    u.pausar()

# ALTERAR ALUNO

def alterar_aluno(sistema):
    u.titulo_menu('ALTERAR ALUNO')

    funcoes = {
        1: lambda a: setattr(a, "nome", u.input_texto('\nNovo Nome: ')),
        2: lambda a: setattr(a, "celular", u.input_celular('\nNovo Celular: ')),
        3: lambda a: setattr(a, "email", u.input_texto('\nNovo Email: '))
    }

    u.alterar_item(
        sistema,
        sistema.alunos,
        "Aluno",
        ARQUIVO_ALUNOS,
        menus.menu_alterar_aluno,
        sistema.opcoes_alterar_aluno,
        funcoes
    )

# EXCLUIR ALUNO

def excluir_aluno(sistema):
    u.titulo_menu('EXCLUIR ALUNO')

    u.excluir_item(
        sistema,
        sistema.alunos,
        "Aluno",
        ARQUIVO_ALUNOS
    )

# VERIFICAR SE EXISTE ALUNO OU CADASTRAR ALUNO

def verificar_cadastrar_aluno(sistema):
    vazio = u.algo_esta_vazio(sistema.alunos, "Aluno")

    if vazio == "n":
        u.mensagem_de_informacao('ATENÇÃO! Operação cancelada!', "AMARELO", "-")
        u.pausar()
        return False

    if vazio == "s":
        cadastrar_aluno(sistema)
        return False

    return True

# CARREGAR ALUNOS JSON

def carregar_json_alunos():
    garantir_arquivo_json(ARQUIVO_ALUNOS)

    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            return [ma.Aluno.from_dict(d) for d in dados]

    except json.JSONDecodeError:
            return []