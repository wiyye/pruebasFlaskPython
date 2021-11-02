from flask import Flask,request,render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def bienvenida():
    return "bienvenido a la página"

if __name__ == "__main__":
    aplicacion.run(debug=True)