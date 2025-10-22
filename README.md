<h1 align="center"> Hominis</h1>

<p align="center">
  <i>Um CRUD Flask moderno com integração de CEP.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Framework-black.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Database-SQLite3-lightgrey.svg" alt="SQLite3">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-yellow.svg" alt="Frontend">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange.svg" alt="Status">
</p>

---

## Sobre o Projeto

**Hominis** é um sistema web desenvolvido com **Flask (Python)** que implementa um **CRUD completo** para gerenciamento de pessoas.  
Além das operações básicas — **criar, visualizar, editar e deletar registros** — o projeto se destaca pela integração com uma **API de CEP**, que preenche automaticamente os campos de endereço, tornando o processo de cadastro rápido e inteligente.

---

## Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| **Backend** | Flask (Python) |
| **Banco de Dados** | SQLite3 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **API Externa** | ViaCEP |

---

## Funcionalidades Principais

✅ Cadastro de pessoas (nome, email, telefone, endereço, etc.)  
✅ Listagem completa dos registros existentes  
✅ Edição e atualização de dados diretamente pela interface  
✅ Exclusão de registros com confirmação visual  
✅ Integração com **API de CEP** para preenchimento automático de endereço  

---

## Arquitetura

O projeto segue uma arquitetura simples e organizada:
- **`app.py`** contém as rotas, inicialização do servidor e integração com o banco de dados.  
- **`templates/`** armazena os arquivos HTML renderizados via Jinja2.  
- **`static/`** guarda os recursos estáticos (CSS e JavaScript).  
- **`instance/hominis..sqlite3.db`** é o banco de dados SQLite, criado automaticamente.

---

## API de CEP

O **Hominis** consome a API pública **ViaCEP**, permitindo preencher automaticamente os campos de endereço a partir do CEP informado:

https://viacep.com.br/ws/{cep}/json/

---

## Autor

**Gustavo Soares Araujo Evangelista dos Anjos**  
 Estudante e desenvolvedor em formação  
 Aprendendo e criando soluções com Python e web development  
