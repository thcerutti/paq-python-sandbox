from flask import Flask
from markupsafe import escape
import csv
from operations import sum
from db import get_client, get_collection

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
        "resultado": sum(num1, num2)
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
    tabelaDeDados = carregarDadosDoArquivo("data/desmatamento_prodes.csv")
    for linha in tabelaDeDados:
        if linha["referencia"] == ano:
            return linha
    return {"erro": "Não encontrado"}, 404

@app.route("/desmatamento/")
def desmatamento_total():
    return carregarDadosDoArquivo("data/desmatamento_prodes.csv")

@app.route("/meu-primeiro-post", methods=["POST"])
def meu_primeiro_post():
    return {"mensagem": "Olá, mundo!"}

@app.route("/loop-for")
def loop_for():
    lista = []
    for i in range(10):
        lista.append(i)
    return {"lista": lista}

@app.route("/loop-while")
def loop_while():
    lista = []
    i = 0
    while i < 15:
        lista.append(i)
        i += 1
    return {"lista": lista}

@app.route("/loop-while-break")
def loop_while_break():
    lista = []
    i = 0
    while i < 15:
        lista.append(i)
        i += 1
        if i == 10:
            break # sai antes do final do loop
    return {"lista": lista}

@app.route("/par-ou-impar/<int:numero>")
def par_ou_impar(numero):
    if numero % 2 == 0:
        return {"mensagem": "par"}
    else:
        return {"mensagem": "ímpar"}

# Exercício de escrita em arquivo .csv
# criar um arquivo novo, receber um valor via parâmetro e escrever esse valor no arquivo

@app.route("/movies")
def movies():
    try:
        client = get_client()
        movie_collection = get_collection(client, "sample_mflix", "movies")
        all_movies = []
        for movie in movie_collection.find({"year": 1995}).limit(10):
            all_movies.append({
                "title": movie["title"],
                "year": movie["year"],
                "plot": movie["plot"],
                "cast": movie["cast"],
                "directors": movie["directors"],
                "genres": movie["genres"],
                "runtime": movie["runtime"],
                "imdb": movie["imdb"],
                "awards": movie["awards"],
                "type": movie["type"]
            })
        return all_movies
    except Exception as e:
        return {"error": str(e)}
