from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    result = 3+4
    return f"<p>Hello from /hello route. 3+4={result}</p>"
