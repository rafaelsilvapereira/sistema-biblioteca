import os

# LIMPA TERMINAL - Independentemente do Sistema Operacional

def limpar_terminal():
    if os.name == 'nt': # Se for Windows
        os.system('cls')
    else: # Se for Linux ou MacOS
        os.system('clear')

# INPUT PAUSAR

def pausar(): input('\nPressione ENTER para continuar...')

# TÍTULO MENUS

def titulo_menu(mensagem):
    print('')
    print('=' * 50)
    print(mensagem.center(50, " "))
    print('=' * 50)
    print('')

# MENSAGENS DE AVISO

def mensagem_aviso(mensagem):
    print('')
    print('-' * 50)
    print(mensagem)
    print('-' * 50)
    print('')

# INPUT ESCOLHER OPÇÕES MENUS

def input_escolher_menu(opcoes):
    while True:
        entrada = input('\nDigite a Opção Desejada: ').strip()

        if not entrada.isdigit():
            mensagem_aviso('AVISO! Digite apenas números.')
            continue

        opcao = int(entrada)

        if opcao not in opcoes:
            mensagem_aviso(f'AVISO! Opção Inválida! Escolha entre as opções: {list(opcoes)}')
            continue

        return opcao

# INPUT TEXTO

def input_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto: return texto

        mensagem_aviso('AVISO! O campo é obrigatório.')

# INPUT NUMERO INTEIRO

def input_inteiro(mensagem):
    while True:
        try:
            numero = int(input_texto(mensagem))

            if numero < 0:
                mensagem_aviso('AVISO! O valor deve ser maior ou igual a "0" zero.')
                continue

            return numero

        except ValueError:
            mensagem_aviso('AVISO! Infome apenas números.')
            continue

# INPUT OPÇÃO DE CONFIRMAÇÃO "Sim" ou "Não" (S/N)

def input_sn(mensagem):
    while True:
        opcao_sn = input(mensagem).strip().lower()

        if opcao_sn in ("s", "n"): return opcao_sn

        mensagem_aviso('AVISO! Opção Inválida! Digite "S" para "Sim" ou "N" para "Não".')

# INPUT CELULAR

def input_celular(mensagem):
    while True:
        celular = input_texto(mensagem).strip()

        if len(celular) == 11 and celular.isdigit():
            return celular

        mensagem_aviso('AVISO! Digite apenas números. Máx. 11 dígitos.')

# VERIFICAR SE ALGO ESTÁ VAZIO

def algo_esta_vazio(algo, texto):
    if not algo:
        opcao = input_sn(f'\nNenhum {texto} cadastrado. Deseja cadastrar agora (S/N)? ')

        return opcao

# VERIFICAR SE ALGO ESTÁ CADASTRADO

def algo_ja_cadastrado(algo, local, texto):
    for a in local:
        if algo.lower() in a.nome.lower() and algo.lower() == a.nome.lower():
            print(f'\n{texto} já cadastrado')
            pausar()
            return True

    return False

# ATUALIZAR STATUS NO CADASTRO

def atualizar_status(quantidade):
    return "Indisponível" if quantidade == 0 else "Disponível"