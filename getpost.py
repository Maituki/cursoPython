from flask import Flask,render_template,redirect,url_for, request

app=Flask(__name__)


#declaracion de ruta principal
@app.route("/")
def hello_world():
    return "pagina inicial"
   
@app.route("/form1", methods=["GET","POST"])                           
def form1():  
    #captamos la información del formulario de forma basica "form"
    if request.method== "POST":
        #2 formas diferentes de hacer el POST
        Nombre = request.form.get("txtNombre")
        email = request.form["txtEmail"]
        return "hola"+Nombre
        #guardarlo en un archivo faltan cosas.
        """ with open("datos.txt"):
            f.write(nombre)
        #clase usuario  pero hay que definirla con sus atributos
        user.nombre=Nombre
        user.email=email
        user.save()
        #otras cosas q se pueden hacer
        if Nombre == "admin" and pwd =="querty":
            return redirect("admin.html")
        else:
            return redirect ("login.html") """
    #es un GET
    else:
        return render_template("form1.html")
 # envia informacion como GET no es recomendable hacerlo pq en la busqueda salen los datos introducidos en el formulario       
""" if request.method== "GET":
     #mostrar informacion por primera vez "args"
     Nombre = request.args.get("txtNombre")
     email = request.args["txtEmail"]
     #no se usa mucho pq no es recomendable 
     return render_template("form1.html?txtNombre"+=nombre)
elif request.method ==¿?preguntar a CHE¿¿
 """
if __name__=="__main__":
    #para no tener que parar el servidor y volverlo a lanzar despues de realizar modificaciones
    app.run(debug=True)