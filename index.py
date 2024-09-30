from flask import Flask
from markupsafe import escape
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>")
def hello(name):
    result = 3+4+1
    return f"<p>Hello from /hello route. 3+4={result}, {escape(name)}!</p>"

@app.route("/soma/<int:num1>/<int:num2>")
def soma(num1, num2):
    resultado = num1 + num2
    return {
        "operacao": "soma",
        "primeiro_valor": num1,
        "segundo_valor": num2,
        "resultado": resultado
    }

def carregarDadosDoArquivo(path):
    dados = []
    with open(path, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)  # Skip the header row
        for row in reader:
            dados.append({
            "referencia": row[0],
            "acre": row[1],
            "amazonas": row[2],
            "amapa": row[3],
            "maranhao": row[4],
            "mato_grosso": row[5],
            "para": row[6],
            "rondonia": row[7],
            "roraima": row[8],
            "tocantins": row[9],
            "area_total_desmatamento": row[10]
            })
    return dados

@app.route("/desmatamento/<int:ano>")
def desmatamento(ano):
    dados = carregarDadosDoArquivo("desmatamento_prodes.csv")
    for dado in dados:
        if int(dado["referencia"]) == ano:
            return dado
    return {"erro": "Não encontrado"}, 404

@app.route("/desmatamento/")
def desmatamento_total():
    dados = carregarDadosDoArquivo("desmatamento_prodes.csv")
    return dados

