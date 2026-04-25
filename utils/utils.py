import os

# CORES E MAIS...

C = {
    "VERDE": "\033[92m",
    "AMARELO": "\033[33m",
    "AZUL": "\033[36m",
    "VERMELHO": "\033[31m",
    "CINZA": "\033[7;30m",
    "INVERTER": "\033[7m",
    "BOLD": "\033[1m",
    "FIM": "\033[0m"
}

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
    limpar_terminal()

    cor_divisor = f'{C['INVERTER']}{C['BOLD']}'
    cor_do_titulo = f'{C['INVERTER']}{C['BOLD']}'
    reset = C['FIM']

    print(f'{cor_divisor}{'=' * 50}{reset}')
    print(f'{cor_do_titulo}{mensagem.center(50, ' ')}{reset}')
    print(f'{cor_divisor}{'=' * 50}{reset}')

# MENSAGEM DE INFORMAÇÃO

def mensagem_de_informacao(texto, cor, tipo_separador):
    divisor = f"{C[cor]}"
    cor_do_texto = f"{C['BOLD']}{C[cor]}"
    reset = C['FIM']

    print(f'\n{divisor}{tipo_separador * 50}{reset}')
    print(f'{cor_do_texto}{texto}{reset}')
    print(f'{divisor}{tipo_separador * 50}{reset}')

# INPUT ESCOLHER OPÇÕES MENUS

def input_escolher_menu(opcoes):
    while True:
        entrada = input('\nDigite a Opção Desejada: ').strip()

        if not entrada.isdigit():
            mensagem_de_informacao('ERRO! Digite apenas números.', "VERMELHO", 'x')
            continue

        opcao = int(entrada)

        if opcao not in opcoes:
            mensagem_de_informacao(f'ATENÇÃO! Opção inválida! Escolha entre as opções: {list(opcoes)}', "AMARELO", '-')
            continue

        return opcao

# INPUT TEXTO

def input_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto: return texto

        mensagem_de_informacao('ATENÇÃO! O campo é obrigatório.', "AMARELO", '-')

# INPUT NUMERO INTEIRO

def input_inteiro(mensagem):
    while True:
        try:
            numero = int(input_texto(mensagem))

            if numero < 0:
                mensagem_de_informacao('ATENÇÃO! O valor deve ser maior ou igual a "0" zero.', "AMARELO", '-')
                continue

            return numero

        except ValueError:
            mensagem_de_informacao('ERRO! Infome apenas números.', "VERMELHO", 'x')
            continue

# INPUT OPÇÃO DE CONFIRMAÇÃO "Sim" ou "Não" (S/N)

def input_sn(mensagem):
    while True:
        opcao_sn = input(mensagem).strip().lower()

        if opcao_sn in ("s", "n"): return opcao_sn

        mensagem_de_informacao('ATENÇÃO! Opção Inválida! Digite "S" para "Sim" ou "N" para "Não".', "AMARELO", '-')

# INPUT CELULAR

def input_celular(mensagem):
    while True:
        celular = input_texto(mensagem).strip()

        if len(celular) == 11 and celular.isdigit():
            return celular

        mensagem_de_informacao('ERRO! Digite apenas números. Máx. 11 dígitos.', "VERMELHO", 'x')

# VERIFICAR SE ALGO ESTÁ VAZIO

def algo_esta_vazio(lista, nome):
    if not lista:
        opcao = input_sn(f'\nNenhum {nome} cadastrado. Deseja cadastrar agora (S/N)? ')

        return opcao

# VERIFICAR SE ALGO ESTÁ CADASTRADO

def algo_ja_cadastrado(algo, local, texto):
    for a in local:
        if algo.lower() in a.nome.lower() and algo.lower() == a.nome.lower():
            mensagem_de_informacao(f'ATENÇÃO! {texto} já cadastrado', "AMARELO", '-')
            pausar()
            return True

    return False

# ATUALIZAR STATUS NO CADASTRO

def atualizar_status(quantidade):
    return "Indisponível" if quantidade == 0 else "Disponível"

# ALTERAR ITEM

def alterar_item(
    sistema,
    lista,
    tipo,
    caminho_arquivo,
    menu_func,
    opcoes,
    funcoes_alteracao
):
    nome = input_texto(f'\nDigite o nome do {tipo}: ')
    
    resultados = sistema.buscar_por_nome(lista, nome)

    if not resultados:
        mensagem_de_informacao(f'ATENÇÃO! Nenhum {tipo} foi localizado.', "AMARELO", "-")
        pausar()
        return

    limpar_terminal()

    titulo_menu(f'RESULTADO DA BUSCA POR "{nome}":')
    for obj in resultados:
        print(f'\n{obj}')

    while True:
        id_obj = input_inteiro(f'\nDigite o ID do {tipo} que deseja alterar: ')

        obj = sistema.buscar_por_id(lista, id_obj)

        if obj and obj in resultados:
            menu_func(obj.nome)

            opcao = input_escolher_menu(opcoes)

            if opcao in funcoes_alteracao:
                funcoes_alteracao[opcao](obj)

                sistema.salvar_json(lista, caminho_arquivo)

                mensagem_de_informacao(f'SUCESSO! {tipo} foi atualizado!', "VERDE", "-")
                pausar()
                return

            else:
                mensagem_de_informacao('ATENÇÃO! Operação cancelada!', "AMARELO", "-")
                pausar()
                return

        mensagem_de_informacao('ERRO! O ID informado não foi localizado!', "VERMELHO", "x")

        opcao_id = input_sn('\nDeseja informar outro ID (S/N)? ')

        if opcao_id == "s": continue

        if opcao_id == "n":
            mensagem_de_informacao('ATENÇÃO! Operação cancelada!', "AMARELO", "-")
            pausar()
            return

# EXCLUIR ITEM

def excluir_item(
    sistema,
    lista,
    tipo,
    caminho_arquivo
):
    nome = input_texto(f'\nDigite o nome do {tipo}: ')

    resultados = sistema.buscar_por_nome(lista, nome)

    if not resultados:
        mensagem_de_informacao(f'ATENÇÃO! Nenhum {tipo} foi localizado.', "AMARELO", "-")
        pausar()
        return

    titulo_menu(f'RESULTADO DA BUSCA POR "{nome}":')
    for obj in resultados:
        print(f'\n{obj}')

    while True:
        id_obj = input_inteiro(f'\nDigite o ID do {tipo} que deseja excluir: ')

        obj = sistema.buscar_por_id(lista, id_obj)

        if obj and obj in resultados:
            opcao = input_sn(f'\nDeseja realmente excluir o {tipo} "{obj.nome}" (S/N)? ')

            if opcao == "n":
                mensagem_de_informacao('ATENÇÃO! Operação cancelada!', "AMARELO", "-")
                pausar()
                return

            lista.remove(obj)

            sistema.salvar_json(lista, caminho_arquivo)

            mensagem_de_informacao(f'SUCESSO! O {tipo} {obj.nome} foi excluído!', "VERDE", '-')
            pausar()
            return

        mensagem_de_informacao('ERRO! O ID informado não foi localizado!', "VERMELHO", "x")

        opcao_id = input_sn('\nDeseja informar outro ID (S/N)? ')

        if opcao_id == "s": continue

        if opcao_id == "n":
            mensagem_de_informacao('ATENÇÃO! Operação cancelada!', "AMARELO", "-")
            pausar()
            return