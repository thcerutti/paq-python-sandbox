from flask import Flask
from markupsafe import escape
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, Pedro and Alice!</h1>"

@app.route("/hello/<name>")
def hello(name):
    result = 3+4+1
    return f"<p>Hello from /hello route. 3+4+1={result}, {escape(name)}!</p>"

@app.route("/soma/<int:num1>/<int:num2>")
def soma(num1, num2):
    return {
        "operacao": "soma",
        "primeiro_valor": num1,
        "segundo_valor": num2,
        "resultado": num1 + num2
    }

def carregarDadosDoArquivo(path):
    dados = []
    with open(path, newline="") as csvfile:
        tabelaDeDados = csv.reader(csvfile, delimiter=",")
        next(tabelaDeDados)  # Skip the header row
        for linha in tabelaDeDados:
            dados.append({
                "referencia": int(linha[0]),
                "acre": linha[1],
                "amazonas": linha[2],
                "amapa": linha[3],
                "maranhao": linha[4],
                "mato_grosso": linha[5],
                "para": linha[6],
                "rondonia": linha[7],
                "roraima": linha[8],
                "tocantins": linha[9],
                "area_total_desmatamento": linha[10]
            })
    return dados

@app.route("/desmatamento/<int:ano>")
def desmatamento(ano):
    tabelaDeDados = carregarDadosDoArquivo("desmatamento_prodes.csv")
    for linha in tabelaDeDados:
        if linha["referencia"] == ano:
            return linha
    return {"erro": "Não encontrado"}, 404

@app.route("/desmatamento/")
def desmatamento_total():
    return carregarDadosDoArquivo("desmatamento_prodes.csv")

