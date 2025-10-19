from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.classes import Base, Alunos

app = Flask(__name__)
CORS(app)

engine = create_engine('sqlite:///estudos1.db')
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return send_from_directory('static','moedas.html')

@app.route('/moedas')
def moedas():
    return send_from_directory('static', 'moedas.html')

@app.route('/eventos')
def eventos():
    return send_from_directory('static', 'eventos.html')

@app.route('/desafios')
def desafios():
    return send_from_directory('static', 'desafios.html')

@app.route('/itens')
def itens():
    return send_from_directory('static', 'itens.html')

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    session = Session()
    alunos = session.query(Alunos).all()
    resultado = [
        {
            'matricula': aluno.matricula,
            'nome': aluno.nome,
            'curso': aluno.curso,
            'wydencoin': aluno.wydencoin
        }
        for aluno in alunos
    ]
    session.close()
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(port=5500, debug=True)
