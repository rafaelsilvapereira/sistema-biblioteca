# 📚 Sistema de Biblioteca

## 📌 Sobre o projeto

Sistema de gerenciamento de biblioteca desenvolvido em Python, com foco em organização de código, separação de responsabilidades e aplicação de boas práticas de desenvolvimento.

O sistema permite o controle de alunos e livros, incluindo cadastro, listagem, empréstimo e devolução.

---

## 🚀 Funcionalidades

* 📖 Cadastro de alunos
* 📚 Cadastro de livros
* 🔄 Empréstimo de livros
* ✅ Devolução de livros
* 📋 Listagem de dados

---

## 🛠 Tecnologias utilizadas

* Python
* JSON (persistência de dados)
* Git e GitHub

---

## ▶️ Como executar o projeto

```bash
git clone https://github.com/rafaelsilvapereira/sistema-biblioteca.git
cd sistema-biblioteca
python main.py
```

---

## ⚙️ Funcionamento dos dados

O sistema utiliza arquivos JSON para armazenar os dados de alunos e livros.

Caso os arquivos não existam, o sistema cria automaticamente os arquivos necessários ao iniciar, garantindo que o projeto funcione corretamente em qualquer ambiente.

---

## 📂 Estrutura do projeto

```
sistema-biblioteca/
│
├── dados/            # Arquivos JSON (armazenamento)
├── models/           # Classes do sistema (Aluno, Livro, Sistema)
├── services/         # Regras de negócio
├── utils/            # Funções auxiliares e menus
│
├── config.py         # Configuração de caminhos e arquivos
├── main.py           # Arquivo principal
```

---

## 🧠 Conceitos aplicados

* Programação Orientada a Objetos (POO)
* Separação de responsabilidades
* Estruturação modular
* Persistência de dados com JSON
* Tratamento de erros

---

## 📈 Melhorias futuras

* Interface gráfica (Tkinter)
* Integração com banco de dados (SQLite)
* Sistema de autenticação
* Melhorias na experiência do usuário

---

## 👨‍💻 Autor

Rafael Silva Pereira
🔗 LinkedIn: https://www.linkedin.com/in/faelpereirars

---

## 📄 Licença

Este projeto está sob a licença MIT.