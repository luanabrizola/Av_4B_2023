from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/dw2'
db = SQLAlchemy(app)

class Passagem(db.Model):
    idpassagem = db.Column(db.Integer, primary_key=True)
    data_ida = db.Column(db.TIMESTAMP, nullable=False)
    data_volta = db.Column(db.TIMESTAMP)
    idorigem = db.Column(db.Integer, nullable=False)
    iddestino = db.Column(db.Integer, nullable=False)
    duracao = db.Column(db.Time, nullable=False)
    idclassevoo = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')

@app.route('/cadastro')
def cadastro():
    return render_template('passagem.html')

@app.route('/bd')
def bd():
    return render_template('bd.html')

@app.route('/conceitos')
def conceitos():
    return render_template('conceitos.html')

@app.route('/passagens')
def listar_passagens():
    passagens = Passagem.query.all()
    return render_template('listagem.html', passagens=passagens)

@app.route('/inserir_passagem', methods=['GET', 'POST'])
def inserir_passagem():
    if request.method == 'POST':
        idpassagem = request.form['idpassagem']
        data_ida = request.form['dataembarque']
        data_volta = request.form['dataretorno']
        idorigem = request.form['origem']
        iddestino = request.form['destino']
        duracao = request.form['duracao']
        idclassevoo = request.form['classe']

        nova_passagem = Passagem(
            idpassagem=idpassagem,
            data_ida=datetime.strptime(data_ida, '%Y-%m-%d').date(),
            data_volta=datetime.strptime(data_volta, '%Y-%m-%d').date(),
            idorigem=idorigem,
            iddestino=iddestino,
            duracao=datetime.strptime(duracao, '%H:%M').time(),
            idclassevoo=idclassevoo
        )

        db.session.add(nova_passagem)
        db.session.commit()

        return redirect(url_for('listar_passagens'))

    return render_template('passagem.html')

if __name__ == '__main__':
    app.run(debug=True)