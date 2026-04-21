from datetime import datetime

import json

from config import ARQUIVO_LIVROS

import dados
import utils.menus as menus
import utils.utils as u
import models.classe_Livro as classe_Livro

# TITULO DOS MENUS

def titulo_menu(mensagem):
    u.limpar_terminal()
    u.titulo_menu(mensagem)

# TITULO SUBMENUS

def titulo(mensagem):
    u.titulo_menu(mensagem)

# CADASTRAR LIVRO

def cadastrar_livro(sistema):
    titulo_menu('CADASTRAR LIVRO')
    
    data_cadastro = datetime.now().strftime("%d/%m/%Y / %H:%M:%S")
    
    nome = u.input_texto('Nome do Livro: ')

    if u.algo_ja_cadastrado(nome, sistema.livros, "Livro"):
        return

    quantidade = u.input_inteiro('\nQuantidade: ')

    id = sistema.gerar_id_livro()
    livro = classe_Livro.Livro(id, data_cadastro, nome, quantidade)
    livro.atualizar_status()
    sistema.adicionar_livro(livro)

    salvar_json_livros(sistema.livros)

    u.mensagem_aviso(f'O Livro {nome} foi cadastrado!')

    u.pausar()

# LISTAR LIVROS

def listar_livros(sistema):
    titulo_menu('LIVROS CADASTRADOS:')

    for livro in sistema.livros:
        print(livro)

    u.pausar()

# ALTERAR LIVRO

def alterar_livro(sistema):
    titulo_menu('ALTERAR LIVRO')

    nome_livro = u.input_texto('Digite o nome do Livro: ')

    resultados = sistema.buscar_livro_nome(nome_livro)

    if len(resultados) == 0:
        titulo(f'RESULTADO DA BUSCA POR "{nome_livro}":')
        print('Nenhum Livro foi localizado.')
        u.pausar()
        return

    else:
        titulo(f'RESULTADO DA BUSCA POR "{nome_livro}":')

        for livro in resultados: print(livro)

    while True:
        encontrado = False # Dentro do While - Cada tentativa começa zerada.

        id_livro = u.input_inteiro('\nDigite o ID do Livro que deseja alterar: ')

        livro = sistema.buscar_livro_por_id(id_livro)

        if livro and livro in resultados:
            encontrado = True
            menus.menu_alterar_livro(livro.nome)

            opcao = u.input_escolher_menu(dados.opcoes_alterar_livro)

            if opcao == 1:
                livro.nome = u.input_texto('\nNovo Nome: ')

                salvar_json_livros(sistema.livros)

                u.mensagem_aviso(f'O nome do livro foi alterado para "{livro.nome}".')

                u.pausar()
                return

            elif opcao == 2:
                livro.quantidade = u.input_inteiro('\nNova Quantidade: ')
                livro.atualizar_status()

                salvar_json_livros(sistema.livros)

                u.mensagem_aviso(f'A quantidade do livro foi alterado para "{livro.quantidade}".')

                u.pausar()
                return

            else:
                print('\nOperação Cancelada.')
                u.pausar()
                return

        if not encontrado:
            u.mensagem_aviso('O ID informado não foi localizado!')

            opcao_id = u.input_sn(f'\nDeseja informar outro ID (S/N)? ')

            if opcao_id == "s": continue

            if opcao_id == "n":
                print('\nOperação Cancelada!')
                u.pausar()
                return

# EXCLUIR LIVRO

def excluir_livro(sistema):
    titulo_menu('EXCLUIR LIVRO')

    nome_livro = u.input_texto('Digite o nome do Livro: ')

    resultados = sistema.buscar_livro_nome(nome_livro)

    if len(resultados) == 0:
        titulo(f'RESULTADO DA BUSCA POR "{nome_livro}":')
        print('Nenhum Livro foi localizado.')
        u.pausar()
        return

    else:
        titulo(f'RESULTADO DA BUSCA POR "{nome_livro}":')

        for livro in resultados: print(livro)

    while True:
        id_livro = u.input_inteiro('\nDigite o ID do Livro que deseja excluir: ')

        livro = sistema.buscar_livro_por_id(id_livro)

        if livro and livro in resultados:
            opcao_sn = u.input_sn(f'\nDeseja realmente excluir o Livro "{livro.nome}" (S/N)? ')

            if opcao_sn == "n":
                print('\nOperação Cancelada!')
                u.pausar()
                return

            if opcao_sn == "s":
                sistema.remover_livro(livro)
                salvar_json_livros(sistema.livros)
                u.mensagem_aviso(f'AVISO: O Livro {livro.nome} foi excluído!')
                u.pausar()
                return

        u.mensagem_aviso('O ID informado não foi localizado!')
        
        opcao_id = u.input_sn(f'\nDeseja informar outro ID (S/N)? ')

        if opcao_id == "s": continue

        if opcao_id == "n":
            print('\nOperação Cancelada!')
            u.pausar()
            return

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

# SALVAR LIVRO JSON - Atualizada

def salvar_json_livros(lista_livros):
    try:
        with open(ARQUIVO_LIVROS, "w", encoding="utf-8") as arquivo:
            json.dump(
                [livro.to_dict() for livro in lista_livros],
                arquivo,
                indent=4,
                ensure_ascii=False
            )
    except Exception as e:
        print(f"Erro ao salvar livros: {e}")

# CARREGAR LIVROS JSON - Atualizada

def carregar_json_livros():
    try:
        with open(ARQUIVO_LIVROS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            return [classe_Livro.Livro.from_dict(d) for d in dados]

    except FileNotFoundError:
        return []

# # SALVAR LIVRO JSON - Antes

# def salvar_json_livros(lista_livros):
#     with open("livros.json", "w", encoding="utf-8") as arquivo:
#         json.dump(
#             [livro.to_dict() for livro in lista_livros],
#             arquivo,
#             indent=4,
#             ensure_ascii=False
#         )

# # CARREGAR LIVROS JSON - Antes

# def carregar_json_livros():
#     try:
#         with open("livros.json", "r", encoding="utf-8") as arquivo:
#             dados = json.load(arquivo)

#             return [classe_Livro.Livro.from_dict(d) for d in dados]

#     except FileNotFoundError:
#         return []