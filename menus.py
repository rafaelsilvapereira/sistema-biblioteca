import utils as u

# MENU PRINCIPAL

def menu_principal():
    # Limpa Terminal
    u.limpar_terminal()

    u.titulo_menu('SISTEMA DE BIBLIOTECA v4.0')
    print('1 - Menu Alunos')
    print('2 - Menu Livros')
    print('3 - Emprestar Livro')
    print('4 - Livros Emprestados')
    print('5 - Devolver Livro')
    print('0 - Sair')

# MENU ALUNOS

def menu_alunos():
    u.limpar_terminal()

    u.titulo_menu('MENU - ALUNOS')
    print('1 - Cadastrar Aluno')
    print('2 - Alterar Aluno')
    print('3 - Excluir Aluno')
    print('4 - Listar Alunos')
    print('0 - Menu Principal')

# MENU LIVROS

def menu_livros():
    # Limpa Terminal
    u.limpar_terminal()

    u.titulo_menu('MENU - LIVROS')
    print('1 - Cadastrar Livro')
    print('2 - Alterar Livro')
    print('3 - Excluir Livro')
    print('4 - Listar Livros')
    print('0 - Menu Principal')

# MENU OPÇÕES DE ALTERAÇÃO ALUNO

def menu_alterar_aluno(nome_aluno):
    print(f'\nQuais dados deseja alterar do aluno "{nome_aluno}"?')
    print('1 - Nome')
    print('2 - Celular')
    print('3 - E-Mail')
    print('0 - Cancelar')

# MENU OPÇÕES DE ALTERAÇÃO LIVRO

def menu_alterar_livro(nome_livro):
    print(f'\nQuais dados deseja alterar do livro "{nome_livro}"?')
    print('1 - Nome')
    print('2 - Quantidade')
    print('0 - Cancelar')