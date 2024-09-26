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
