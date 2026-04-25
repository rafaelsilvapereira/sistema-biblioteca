import utils.menus as menus
import utils.utils as u
import models.sistema as sistema
import services.funcoes_alunos as fa
import services.funcoes_livros as fl
import services.funcoes_emprestimos as fe

# ========================================
# PROGRAMA PRINCIPAL
# ========================================

# Criar Sistema
sistema = sistema.SistemaBiblioteca()

# Carregar JSON Alunos e IDs
sistema.alunos = fa.carregar_json_alunos()
sistema.carregar_ids_aluno()

# Carregar JSON Livros e IDs
sistema.livros = fl.carregar_json_livros()
sistema.carregar_ids_livro()

# Carregar JSON Emprestados e IDs
sistema.emprestimos = fe.carregar_json_emprestimos()
sistema.carregar_ids_emprestimo()

while True:
    # Menu Principal
    menus.menu_principal()

    menu_principal = u.input_escolher_menu(sistema.opcoes_menu_principal)

    if menu_principal == 1:
        while True:
            # Menu Alunos
            menus.menu_alunos()

            menu_alunos = u.input_escolher_menu(sistema.opcoes_menu_alunos)

            if menu_alunos == 1: fa.cadastrar_aluno(sistema)

            elif menu_alunos  == 2:
                if not fa.verificar_cadastrar_aluno(sistema): continue
                
                fa.alterar_aluno(sistema)

            elif menu_alunos  == 3:
                if not fa.verificar_cadastrar_aluno(sistema): continue
                
                fa.excluir_aluno(sistema)

            elif menu_alunos  == 4:
                if not fa.verificar_cadastrar_aluno(sistema): continue

                fa.listar_alunos(sistema)

            elif menu_alunos  == 0:
                break
    
    elif menu_principal == 2:
        while True:
            # Menu Livros
            menus.menu_livros()

            menu_livros = u.input_escolher_menu(sistema.opcoes_menu_livros)

            if menu_livros == 1: fl.cadastrar_livro(sistema)

            elif menu_livros == 2:
                if not fl.verificar_cadastrar_livro(sistema): continue
                
                fl.alterar_livro(sistema)

            elif menu_livros == 3:
                if not fl.verificar_cadastrar_livro(sistema): continue
                
                fl.excluir_livro(sistema)

            elif menu_livros == 4:
                if not fl.verificar_cadastrar_livro(sistema): continue

                fl.listar_livros(sistema)

            elif menu_livros == 0:
                break
    
    elif menu_principal == 3:
        if not fl.verificar_cadastrar_livro(sistema): continue

        fe.emprestar_livro(sistema)

    elif menu_principal == 4:
        if not fl.verificar_cadastrar_livro(sistema): continue

        fe.listar_livros_emprestados(sistema)

    elif menu_principal == 5: ...

    elif menu_principal == 0:
        print('\nSAINDO DO SISTEMA...')
        print('')
        break