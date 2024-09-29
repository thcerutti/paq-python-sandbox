from flask import Flask
from markupsafe import escape

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

def ler_arquivo(path):
    with open(path, "r") as file:
        return file.read()

@app.route("/desmatamento/<int:ano>")
def desmatamento(ano):
    path = "desmatamento_prodes.csv"
    dados = ler_arquivo(path)
    return {
        "ano": ano,
        "dados": dados
    }

