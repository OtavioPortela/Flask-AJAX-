from flask import Blueprint, render_template, request, jsonify


main = Blueprint('main', __name__)

nomes = []

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/salvar', methods=['POST'])
def salvar():
    nome = request.json.get('nome')
    if nome:
        nomes.append(nome)
        return jsonify({'status': 'sucesso', 'nomes': nomes,})
    return jsonify({'status': 'ERRO', 'nomes': 'Nome Vazio',}), 400


@main.route('/testar', methods=['POST'])
def testar():
    teste = 5
    return jsonify({'status': 'sucesso', 'apagar': 'CHUCHU',})


@main.route('/sugestoes')
def sugestoes():
    termo = request.args.get('termo', '').lower()
    lista = [
    "otavio", "rebeca", "renato", "rita", "roberto", "ricardo", "rafael", "rogerio",
    "ana", "joão", "maria", "josé", "pedro", "marcos", "aline", "beatriz", "carlos",
    "daniela", "eduardo", "fernanda", "gabriel", "helena", "igor", "juliana", "karla",
    "lucas", "matheus", "natalia", "olivia", "paulo", "quiteria", "rafaela", "samuel",
    "tania", "ursula", "valeria", "william", "xavier", "yasmin", "zuleica", "breno",
    "bruna", "caio", "carla", "daniel", "elisa", "fabio", "gustavo", "isabela", "jorge",
    "lara", "miguel"
    ]
    sugestoes_filtradas = [nome for nome in lista if termo in nome.lower()]
    
    return jsonify({'sugestoes': sugestoes_filtradas})
    