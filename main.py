from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/listar")
def listar():
    con = sqlite3.connect('pokemom.db')
    cur = con.cursor()
    sql_select = 'select * from pokeagenda'
    cur.execute(sql_select)
    dados = cur.fetchall()
    con.close()
    return render_template('listar.html',dados = dados)

if __name__ == "__main__":
    app.run()


