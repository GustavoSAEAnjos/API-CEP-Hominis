# Importação das bibliotecas essenciais para a aplicação web
# Flask: framework principal para criação de rotas, renderização de templates e manipulação de requisições
# SQLAlchemy: biblioteca ORM para interação com banco de dados relacional
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Inicialização da aplicação Flask e configuração do banco de dados SQLite
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"
app.secret_key = "crud_cursos_super_secreta_e_forte"
db = SQLAlchemy(app)

# Modelo de dados: Curso
class Curso(db.Model):
    id_curso = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)

    def __init__(self, nome_curso, descricao, carga_horaria):
        self.nome_curso = nome_curso
        self.descricao = descricao
        self.carga_horaria = carga_horaria

# Rota inicial
@app.route("/")
def principal():
    return render_template("index.html")

# Listagem paginada de cursos
@app.route("/listar")
def listar():
    return render_template("listar.html")

# Cadastro de novo curso
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    return render_template("cadastrar.html")

# Exclusão de curso
@app.route("/excluir", methods=["GET", "POST"])
def excluir():
    return redirect(url_for("listar"))

# Edição de curso
@app.route("/editar", methods=["GET", "POST"])
def editar():
    return render_template("editar.html")

# Inicialização da aplicação
if __name__ == "__main__":
    # Cria as tabelas no banco caso ainda não existam
    with app.app_context():
        db.create_all()

    # Inicia o servidor Flask em modo de desenvolvimento
    app.run(debug=True)
