import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DADOS_DIR = os.path.join(BASE_DIR, 'dados')

ARQUIVO_ALUNOS = os.path.join(DADOS_DIR, 'alunos.json')

ARQUIVO_LIVROS = os.path.join(DADOS_DIR, 'livros.json')

ARQUIVO_EMPRESTIMOS = os.path.join(DADOS_DIR, 'emprestimos.json')

# CRIA ARQUIVO JSON

def garantir_arquivo_json(caminho):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)