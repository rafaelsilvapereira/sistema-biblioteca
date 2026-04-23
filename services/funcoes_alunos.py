import json

from config import ARQUIVO_ALUNOS, garantir_arquivo_json

import dados
import utils.menus as menus
import utils.utils as u
import models.aluno as ma

# TITULO DOS MENUS

def titulo_menu(mensagem):
    u.limpar_terminal()
    u.titulo_menu(mensagem)

# TITULO SUBMENUS

def titulo(mensagem):
    u.titulo_menu(mensagem)

# CADASTRAR ALUNO

def cadastrar_aluno(sistema):
    titulo_menu('CADASTRAR ALUNO')

    nome = u.input_texto('Nome do Aluno: ')

    if u.algo_ja_cadastrado(nome, sistema.alunos, "Aluno"):
        return

    celular = u.input_celular('\nCelular (Máx. 11 dígitos): ')

    email = u.input_texto('\nE-Mail: ')

    id = sistema.gerar_id_aluno()
    aluno = ma.Aluno(id, nome, celular, email)
    sistema.adicionar_aluno(aluno)

    sistema.salvar_json(sistema.alunos, ARQUIVO_ALUNOS)

    u.mensagem_aviso(f'O Aluno "{nome}" foi cadastrado!')
    
    u.pausar()

# LISTAR ALUNOS

def listar_alunos(sistema):
    titulo_menu('ALUNOS CADASTRADOS:')

    for aluno in sistema.alunos:
        print(aluno)

    u.pausar()

# ALTERAR ALUNO

def alterar_aluno(sistema):
    titulo_menu('ALTERAR ALUNO')

    nome_aluno = u.input_texto('Digite o nome do Aluno: ')

    resultados = sistema.buscar_por_nome(sistema.alunos, nome_aluno)

    #resultados = sistema.buscar_aluno_nome(nome_aluno)

    if len(resultados) == 0:
        titulo(f'RESULTADO DA BUSCA POR "{nome_aluno}":')
        print('Nenhum Aluno foi localizado.')
        u.pausar()
        return

    else:
        titulo(f'RESULTADO DA BUSCA POR "{nome_aluno}":')

        for aluno in resultados: print(aluno)

    while True:
        encontrado = False # Dentro do While - Cada tentativa começa zerada.

        id_aluno = u.input_inteiro('\nDigite o ID do Aluno que deseja alterar: ')

        aluno = sistema.buscar_por_id(sistema.alunos, id_aluno)

        if aluno and aluno in resultados:
            encontrado = True
            menus.menu_alterar_aluno(aluno.nome)

            opcao = u.input_escolher_menu(dados.opcoes_alterar_aluno)

            if opcao == 1:
                aluno.nome = u.input_texto('\nNovo Nome: ')

                sistema.salvar_json(sistema.alunos, ARQUIVO_ALUNOS)

                u.mensagem_aviso(f'O nome do aluno foi alterado para "{aluno.nome}".')

                u.pausar()
                return

            elif opcao == 2:
                aluno.celular = u.input_celular('\nNovo Celular: ')

                sistema.salvar_json(sistema.alunos, ARQUIVO_ALUNOS)

                u.mensagem_aviso(f'O celular do aluno foi alterado para "{aluno.celular}".')

                u.pausar()
                return

            elif opcao == 3:
                aluno.email = u.input_texto('\nNovo Email: ')

                sistema.salvar_json(sistema.alunos, ARQUIVO_ALUNOS)

                u.mensagem_aviso(f'O e-mail do aluno foi alterado para "{aluno.email}".')

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

# EXCLUIR ALUNO - Atualizado

def excluir_aluno(sistema):
    titulo_menu('EXCLUIR ALUNO')

    u.excluir_item(
        sistema,
        sistema.alunos,
        "Aluno",
        ARQUIVO_ALUNOS
    )

# # EXCLUIR ALUNO (Anterior)

# def excluir_aluno(sistema):
#     titulo_menu('EXCLUIR ALUNO')

#     nome_aluno = u.input_texto('Digite o nome do Aluno: ')

#     resultados = sistema.buscar_por_nome(sistema.alunos, nome_aluno)

#     if len(resultados) == 0:
#         titulo(f'RESULTADO DA BUSCA POR "{nome_aluno}":')
#         print('Nenhum Aluno foi localizado.')
#         u.pausar()
#         return

#     else:
#         titulo(f'RESULTADO DA BUSCA POR "{nome_aluno}":')

#         for aluno in resultados: print(aluno)

#     while True:
#         id_aluno = u.input_inteiro('\nDigite o ID do Aluno que deseja excluir: ')

#         aluno = sistema.buscar_por_id(sistema.alunos, id_aluno)

#         if aluno and aluno in resultados:
#             opcao_sn = u.input_sn(f'\nDeseja realmente excluir o Aluno "{aluno.nome}" (S/N)? ')

#             if opcao_sn == "n":
#                 print('\nOperação Cancelada!')
#                 u.pausar()
#                 return

#             if opcao_sn == "s":
#                 sistema.remover_aluno(aluno)
#                 sistema.salvar_json(sistema.alunos, ARQUIVO_ALUNOS)
#                 u.mensagem_aviso(f'AVISO: O Aluno {aluno.nome} foi excluído!')
#                 u.pausar()
#                 return

#         u.mensagem_aviso('O ID informado não foi localizado!')
        
#         opcao_id = u.input_sn(f'\nDeseja informar outro ID (S/N)? ')

#         if opcao_id == "s": continue

#         if opcao_id == "n":
#             print('\nOperação Cancelada!')
#             u.pausar()
#             return

# VERIFICAR SE EXISTE ALUNO OU CADASTRAR ALUNO

def verificar_cadastrar_aluno(sistema):
    vazio = u.algo_esta_vazio(sistema.alunos, "Aluno")

    if vazio == "n":
        print('\nOperação Cancelada!')
        u.pausar()
        return False

    if vazio == "s":
        cadastrar_aluno(sistema)
        return False

    return True

# # SALVAR JSON - Atualizada (Qualquer Pasta)

# def salvar_json(lista_objetos, caminho_arquivo):
#     try:
#         with open(caminho_arquivo, "w", encoding="utf-8") as f:
#             json.dump([obj.to_dict() for obj in lista_objetos], f, indent=4, ensure_ascii=False)
#     except Exception as e:
#         print(f"Erro ao salvar alunos: {e}")

# # SALVAR ALUNO JSON - Anterior (Qualquer Pasta)

# def salvar_json_alunos(lista_alunos):
#     try:
#         with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as arquivo:
#             json.dump(
#                 [aluno.to_dict() for aluno in lista_alunos],
#                 arquivo,
#                 indent=4,
#                 ensure_ascii=False
#             )
#     except Exception as e:
#         print(f"Erro ao salvar alunos: {e}")

# # SALVAR ALUNO JSON (Qualquer Pasta)

# def salvar_json_alunos(lista_alunos):
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     caminho = os.path.join(BASE_DIR, '..', 'dados', 'alunos.json')

#     with open(caminho, "w", encoding="utf-8") as arquivo:
#         json.dump(
#             [aluno.to_dict() for aluno in lista_alunos],
#             arquivo,
#             indent=4,
#             ensure_ascii=False
#         )

# # SALVAR ALUNO JSON (Mesma Pasta)

# def salvar_json_alunos(lista_alunos):
#     with open("alunos.json", "w", encoding="utf-8") as arquivo:
#         json.dump(
#             [aluno.to_dict() for aluno in lista_alunos],
#             arquivo,
#             indent=4,
#             ensure_ascii=False
#         )

# CARREGAR ALUNOS JSON (Atualizada)

def carregar_json_alunos():
    garantir_arquivo_json(ARQUIVO_ALUNOS)

    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            return [ma.Aluno.from_dict(d) for d in dados]

    except json.JSONDecodeError:
            return []

    # except FileNotFoundError:
    #     return []

# # CARREGAR ALUNOS JSON (Anterior)

# def carregar_json_alunos():
#     try:
#         with open("alunos.json", "r", encoding="utf-8") as arquivo:
#             dados = json.load(arquivo)

#             return [classe_Aluno.Aluno.from_dict(d) for d in dados]

#     except FileNotFoundError:
#         return []