from flask import Flask, render_template

import mysql.connector
from controller import medico_controller

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="290380",
    database="agendamento_medico"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/medico", methods=["GET", "POST"])
def medico():
    return medico_controller.cadastrar_medico()

if __name__ == "__main__":
    app.run(debug=True)

 