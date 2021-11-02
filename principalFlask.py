from flask import Flask,request,render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def bienvenida():
    return "bienvenido a la página"

@aplicacion.route("/martes")
def metodoMartes():
    return "es el segundo día de la semana"

@aplicacion.route("/python")
def metodoPython():
    return "es un lenguaje de programación"

@aplicacion.route("/concepto")
def conceptoS():
    elconcepto=request.args.get("laVariable1")
    if elconcepto=="bit":
        return "unidad minima de informacion con valores 0 o 1"
    elif elconcepto == "byte":
        return "equivale a 8 bits"
    elif elconcepto == "perrito":
        return "mejor amigo del hombre"
    else:
        return "concepto no encontrado"    


@aplicacion.route("/conHtmlNoPlantilla")
def metodoHtml():
    return "<h1>prueba de formato html</h1>"


@aplicacion.route("/conHtmlSiPlantilla")
def metodoHtml2():
    return render_template("prueba.html")

    

if __name__ == "__main__":
    aplicacion.run(debug=True)