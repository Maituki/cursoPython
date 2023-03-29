from flask import Flask, render_template 

app = Flask(__name__)

class Empleado:
     def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


#declaracion ruta principal y función. La princiaqpl va "/"
@app.route("/")
def helloKitty():
    #instanciamos
    jon = Empleado("Jon", "Gomez", 25)
    #paso el objeto completo
    return render_template("index.html", empleado=jon)
#hacerlo por atributos 
    return render_template("index.html", nombre=jon.nombre, edad=jon.edad)

#declaro otra ruta para la nueva pagina. Asi con el resto de funciones. cada función es una pagina web
@app.route("/holanuevo")
def holanuevo():
    return render_template("index.html")

@app.route("/adiosnuevo")
def adiosnuevo():
    return render_template("adios.html")

@app.route("/adios")
def adios():
    #variable nueva q no hay q declarar
    shtml="<h1>Adios</h1>"
    shtml=shtml+ "<h2>Otro Adios</h2>"
    return shtml

if __name__=="__main__":
    app.run()