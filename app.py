from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hominis.sqlite3"
app.secret_key = "senha_padrao_projeto_flask_hominis_12345"
db = SQLAlchemy(app)


class hominis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    cpf = db.Column(db.Text, nullable=False)
    data_nasc_fund = db.Column(db.Text, nullable=False)
    genero = db.Column(db.Text, nullable=True)
    estado_civil = db.Column(db.Text, nullable=True)
    nacionalidade = db.Column(db.Text, nullable=True)
    ocupaçao = db.Column(db.Text, nullable=False)
    telefone_principal = db.Column(db.Text, nullable=False)
    telefone_secundario = db.Column(db.Text, nullable=True)
    email_prncipal = db.Column(db.Text, nullable=False)
    email_secundario = db.Column(db.Text, nullable=True)
    cep = db.Column(db.Text, nullable=False)
    logradouro = db.Column(db.Text, nullable=False)
    numero_casa = db.Column(db.Text, nullable=False)
    complemento = db.Column(db.Text, nullable=True)
    bairro = db.Column(db.Text, nullable=False)
    cidade = db.Column(db.Text, nullable=False)
    estado = db.Column(db.Text, nullable=False)
    pais = db.Column(db.Text, nullable=False)
    senha = db.Column(db.Text, nullable=False)

    def __init__(self, nome, cpf, data_nasc_fund, genero, estado_civil, nacionalidade,
                 ocupaçao, telefone_principal, telefone_secundario, email_prncipal,
                 email_secundario, cep, logradouro, numero_casa, complemento,
                 bairro, cidade, estado, pais, senha):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc_fund = data_nasc_fund
        self.genero = genero
        self.estado_civil = estado_civil
        self.nacionalidade = nacionalidade
        self.ocupaçao = ocupaçao
        self.telefone_principal = telefone_principal
        self.telefone_secundario = telefone_secundario
        self.email_prncipal = email_prncipal
        self.email_secundario = email_secundario
        self.cep = cep
        self.logradouro = logradouro
        self.numero_casa = numero_casa
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.senha = senha

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("principal"))

    return render_template("login.html")

@app.route("/index")
def principal():
    return render_template("index.html")


@app.route("/listar")
def listar():
    return render_template("listar.html")


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    return render_template("cadastrar.html")


@app.route("/excluir", methods=["GET", "POST"])
def excluir():
    return redirect(url_for("listar"))


@app.route("/editar", methods=["GET", "POST"])
def editar():
    return render_template("editar.html")


if __name__ == "__main__":
    # Cria as tabelas no banco caso ainda não existam
    with app.app_context():
        db.create_all()
        admin = hominis.query.filter_by(cpf='00000000000').first()
        if not admin:
            admin = hominis(
                nome="Administrador",
                cpf="00000000000",
                data_nasc_fund="0000-00-00",
                genero="Nenhum",
                estado_civil="Nenhum",
                nacionalidade="Nenhuma",
                ocupaçao="Administrador",
                telefone_principal="(00) 00000-0000",
                telefone_secundario=None,
                email_prncipal="Nenhum",
                email_secundario=None,
                cep="00000-000",
                logradouro="Nenhum",
                numero_casa="0",
                complemento=None,
                bairro="Nenhum",
                cidade="Nenhum",
                estado="Nenhum",
                pais="Nenhum",
                senha="admin123"
            )
            db.session.add(admin)
            db.session.commit()

    app.run(debug=True)
