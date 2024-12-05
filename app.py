from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Leonardo Martins v1.0"