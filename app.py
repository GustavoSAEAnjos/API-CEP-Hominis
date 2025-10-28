from flask import Flask, render_template, request, redirect, url_for, flash, session
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
    if 'usuario_id' in session:
        return redirect(url_for('principal'))
    
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        if not email or not email:
            flash("Por favor, preencha todos os campos.", "error")
        else:
            usuario = hominis.query.filter_by(email_prncipal=email, senha=senha).first()
            if usuario:
                session['usuario_id'] = usuario.id
                session['usuario_nome'] = usuario.nome
                return redirect(url_for("principal"))
            
        flash("Email ou Senha inválidos", "error")

        return render_template("login.html")
    
    return render_template("login.html")

@app.route("/index")
def principal():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    funcionarios = hominis.query.all()
    return render_template("index.html", funcionarios=funcionarios)

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        if not request.form["nome"] or not request.form["cpf"] or not request.form["data_nasc_fund"] or not request.form["ocupacao"] or not request.form["telefone_principal"] or not request.form["emai_secundario"] or not request.form["cep"] or not request.form["log"] or not request.form["numero"] or not request.form["bairro"] or not request.form["cidade"] or not request.form["estado"] or not request.form["pais"] or not request.form["senha"]:
            flash("Por favor, preencha todos os campos obrigatórios.", "error")
        else:
            funcionario = hominis(
                nome=request.form["nome"],
                cpf=request.form["cpf"],
                data_nasc_fund=request.form["data_nasc_fund"],
                genero=request.form["genero"],
                estado_civil=request.form["estado-civil"],
                nacionalidade=request.form["nacionalidade"],
                ocupaçao=request.form["ocupacao"],
                telefone_principal=request.form["telefone_principal"],
                telefone_secundario=request.form["telefone_secundario"],
                email_prncipal=request.form["email_principal"],
                email_secundario=request.form["emai_secundario"],
                cep=request.form["cep"],
                logradouro=request.form["log"],
                numero_casa=request.form["numero"],
                complemento=request.form["complemento"],
                bairro=request.form["bairro"],
                cidade=request.form["cidade"],
                estado=request.form["estado"],
                pais=request.form["pais"],
                senha=request.form["senha"]
            )
            db.session.add(funcionario)
            return redirect(url_for("principal"))
        
    return render_template("cadastrar.html")


@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    funcionario = hominis.query.get_or_404(id)  
    db.session.delete(funcionario)              
    db.session.commit()                         

    flash("Funcionário excluído com sucesso!", "success")
    return redirect(url_for("principal"))


@app.route("/ver/<int:id>")
def ver(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    funcionario = hominis.query.get_or_404(id)
    funcionarios = hominis.query.all()

    return render_template("ver.html", funcionario=funcionario, funcionarios=funcionarios)

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    if id == 1:
        flash("O administrador não pode ser editado.", "error")
        return redirect(url_for("principal"))
    

    funcionario = hominis.query.get_or_404(id)
    funcionarios = hominis.query.all()
    if request.method == "POST":
        if not request.form["nome"] or not request.form["cpf"] or not request.form["data_nasc_fund"] or not request.form["ocupacao"] or not request.form["telefone_principal"] or not request.form["emai_secundario"] or not request.form["cep"] or not request.form["log"] or not request.form["numero"] or not request.form["bairro"] or not request.form["cidade"] or not request.form["estado"] or not request.form["pais"] or not request.form["senha"]:
            flash("Por favor, preencha todos os campos obrigatórios.", "error")
        else:
            funcionario.nome=request.form["nome"]
            funcionario.cpf=request.form["cpf"]
            funcionario.data_nasc_fund=request.form["data_nasc_fund"]
            funcionario.genero=request.form["genero"]
            funcionario.estado_civil=request.form["estado-civil"]
            funcionario.nacionalidade=request.form["nacionalidade"]
            funcionario.ocupaçao=request.form["ocupacao"]
            funcionario.telefone_principal=request.form["telefone_principal"]
            funcionario.telefone_secundario=request.form["telefone_secundario"]
            funcionario.email_prncipal=request.form["email_principal"]
            funcionario.email_secundario=request.form["emai_secundario"]
            funcionario.cep=request.form["cep"]
            funcionario.logradouro=request.form["log"]
            funcionario.numero_casa=request.form["numero"]
            funcionario.complemento=request.form["complemento"]
            funcionario.bairro=request.form["bairro"]
            funcionario.cidade=request.form["cidade"]
            funcionario.estado=request.form["estado"]
            funcionario.pais=request.form["pais"]
            funcionario.senha=request.form["senha"]
            db.session.commit()
            return redirect(url_for("principal"))
        

    return render_template("editar.html", id=id, funcionario=funcionario, funcionarios=funcionarios)

@app.route("/sair")
def sair():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('login'))

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
                email_prncipal="adm@gmail.com",
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
