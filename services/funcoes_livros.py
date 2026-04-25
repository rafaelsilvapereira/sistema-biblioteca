from datetime import datetime

import json

from config import ARQUIVO_LIVROS, garantir_arquivo_json

import utils.menus as menus
import utils.utils as u
import models.livro as ml

# CADASTRAR LIVRO

def cadastrar_livro(sistema):
    u.titulo_menu('CADASTRAR LIVRO')

    data_cadastro = datetime.now().strftime("%d/%m/%Y / %H:%M:%S")

    nome = u.input_texto('\nNome do Livro: ')

    if u.algo_ja_cadastrado(nome, sistema.livros, "Livro"): return

    quantidade = u.input_inteiro('\nQuantidade: ')

    id = sistema.gerar_id_livro()

    livro = ml.Livro(id, data_cadastro, nome, quantidade)

    livro.atualizar_status()

    sistema.adicionar_livro(livro)

    sistema.salvar_json(sistema.livros, ARQUIVO_LIVROS)

    u.mensagem_de_informacao(f'SUCESSO! O Livro {nome} foi cadastrado!', "VERDE", "-")

    u.pausar()

# LISTAR LIVROS

def listar_livros(sistema):
    u.titulo_menu('LIVROS CADASTRADOS:')

    for livro in sistema.livros:
        print(f'\n{livro}')

    u.pausar()

# ALTERAR LIVRO

def alterar_livro(sistema):
    u.titulo_menu('ALTERAR LIVRO')

    funcoes = {
        1: lambda l: setattr(l, "nome", u.input_texto('\nNovo Nome: ')),
        2: lambda l: [
            setattr(l, "quantidade", u.input_inteiro('\nNova Quantidade: ')),
            l.atualizar_status()
        ]
    }

    u.alterar_item(
        sistema,
        sistema.livros,
        "Livro",
        ARQUIVO_LIVROS,
        menus.menu_alterar_livro,
        sistema.opcoes_alterar_livro,
        funcoes
    )

# EXCLUIR LIVRO

def excluir_livro(sistema):
    u.titulo_menu('EXCLUIR LIVRO')

    u.excluir_item(
        sistema,
        sistema.livros,
        "Livro",
        ARQUIVO_LIVROS
    )

# VERIFICAR SE EXISTE LIVRO OU CADASTRAR LIVRO

def verificar_cadastrar_livro(sistema):
    vazio = u.algo_esta_vazio(sistema.livros, "Livro")

    if vazio == "n":
        print('\nOperação Cancelada!')
        u.pausar()
        return False

    if vazio == "s":
        cadastrar_livro(sistema)
        return False

    return True

# CARREGAR LIVROS JSON

def carregar_json_livros():
    garantir_arquivo_json(ARQUIVO_LIVROS)

    try:
        with open(ARQUIVO_LIVROS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            return [ml.Livro.from_dict(d) for d in dados]

    except FileNotFoundError:
        return []