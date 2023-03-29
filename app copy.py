from flask import Flask,render_template,redirect,url_for, request

app=Flask(__name__)


class Coche:
    def __init__(self,id,modelo,año,imagen,descripcion,precio_contado,precio_financiado):
        self.id=id
        self.modelo=modelo
        self.año=año
        self.imagen=imagen
        self.descripcion=descripcion
        self.precio_contado=precio_contado
        self.precio_financiado=precio_financiado
        
listaCoches=[]
peugeot=Coche(1,"Peugeot 308",2023,"peugeot.jpg","308 1.2 PureTech S&S Allure Pack",22900,19913)
audi=Coche(2,"Audi A5",2022,"audi.jpg","AS Sportback 2.0 TFSI 140 KW",25900,23900)
renault=Coche(3,"Renault megane",2021,"renault.jpg","Megane 1.5dCi Energy Intens 66KW",12300,10000)
listaCoches.append(peugeot)
listaCoches.append(audi)
listaCoches.append(renault)

#declaracion de ruta principal
@app.route("/")
def hello_world():
    return render_template("index.html")
#no encuentra el coche direccionamos a pag web noencontrado.html
@app.route("/noencontrado")
def noencontrado():
    return render_template("noencontrado.html")

@app.route("/coches")
def coches():
    return render_template("coches.html",coches=listaCoches)

@app.route("/coche/<int:id>")
def coche(id):
    encontrado=False
    for coche in listaCoches:
        if coche.id==id:
            return render_template("coche.html",coche=coche)
            encontrado=True
            break
    if encontrado==False:
        return redirect(url_for("noencontrado")) 
   
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