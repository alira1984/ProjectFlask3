from flask import Flask, render_template, url_for, request, redirect, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import FormContato

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b28552b2797bb3:c9b462f1@us-cdbr-east-06.cleardb.net/heroku_8d34e36aebad71e'   # Rota para criação do Banco de dados MySQL
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '6c07e1e4d0172b32dbc8216dbb032f96'   # Criação de chave de segurança para csrf token




class Contato(db.Model):   # Criação dos dados do banco de dados MySQL
    __tablename__ = 'Contatos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    assunto = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)


    def __init__(self, nome, email, assunto, descricao):
        self.nome = nome
        self.email = email
        self.assunto = assunto
        self.descricao = descricao

db.create_all()

class Meus_projetos:
    def __init__(self, empresa, nome_projeto, semestre,data):
        self.empresa = empresa
        self.nome_projeto = nome_projeto
        self.semestre = semestre
        self.data = data
projeto1 = Meus_projetos("FATEC", "CPUsFatec", "Primeiro semestre", 2020)
projeto2 = Meus_projetos("GSW", "DashBoard", "Segundo semestre", 2021)
projeto3 = Meus_projetos("Ionic", "CRM", "Terceiro semestre", 2021)

projeto = []
projeto.append(projeto1)
projeto.append(projeto2)
projeto.append(projeto3)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download')   #Função para fazer download do currículo
def download_curriculo():
    curriculo = "CURRÍCULO.pdf"
    return send_file(curriculo, as_attachment=True)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/portifolio')
def portifolio():


    return render_template('portifolio.html', projeto=projeto)

@app.route('/contato', methods=['GET', 'POST'])   # Função do formulário de contato.
def contato():
    formcontato = FormContato()
    if formcontato.validate_on_submit() and 'botao_submit' in request.form:
        # Função para passar as informações do formulário para o banco de dados.
        c = Contato(nome=formcontato.nome.data, email=formcontato.email.data, assunto=formcontato.assunto.data, descricao=formcontato.descricao.data)
        db.session.add(c)
        db.session.commit()


        flash(f'Mensagem enviada com sucesso para Anderson Lira', 'alert-success')
        return redirect(url_for('home'))

    return render_template('contato.html', formcontato=formcontato)

if __name__ == '__main__':
    app.run(debug=False)

