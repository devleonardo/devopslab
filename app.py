from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Leonardo Martins v1.0 - Lab Concluído"
