
from flask import Flask, g
import sqlite3

DATABASE = "blog.bd"
SECRET_KEY = "1234"

#app = Flask("Hello")
app = Flask("__name__")
app.config.from_object(__name__)

def conectar_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.bd = conectar_db()

@app.teardown_request  # quando for dar a resposta da requisição
def fim_requisicao(exc):   # exc = erro (se der erro)
    g.bd.close()


@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd .execute(sql)
    entradas = []
    return str(entradas)


#def home():
#    return "<h1><i><u>Hello from Flask</u></i></h1>"

#print("Hello World")
