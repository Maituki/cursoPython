from flask import Flask,render_template,redirect,url_for, request
from flask_sqlalchemy import *
import os

app=Flask(__name__)

#RUTA
basedir = os.path.abspath(os.path.dirname(__file__))
#dobnde va a colgar la bd sqlite y la bd se llama database.db
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'menu.db')
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
#iniciamos
#db.init_app(app)
# hereda de la clase Base definida con ORM gestiona b.d - metodos y atributos q nos permite guardar en una b.d 
#definimos la tabla. Hay q declarar

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    precio = db.Column(db.Integer,nullable=False )
    categoria = db.Column(db.String(60), nullable=False)
    # que hace la variable activo: para no borrar la base datos - historico, analisis información. False es lo q borraste
    activo =db.Column(db.Boolean, default=True)
  
    #es una funcion de la clase Menu - en concreto el constructor
    def __init__(self, nombre, descripcion, precio, categoria, activo):
        self.nombre= nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.activo = True

#creamos la base de datos
with app.app_context():
    db.create_all()

#declaracion de ruta principal
""" @app.route("/")
def mostrar_platos():
    platos = Menu.query.all() """

#@app.route("/admin_platos")     
#def admin_platos():   

@app.route("/insertar_comida", methods=["GET","POST"])                           
def insertar_comida():  
    #captamos la información del formulario de forma basica "form"
    #AL DAR AL BOTON AÑADIR ESTAMOS UTILIZANDO EL "POST"
    if request.method== "POST":
        #2 formas diferentes de hacer el POST
        nombre = request.form.get("txtNombre")
        descripcion = request.form.get("txtDescripcion")
        precio = float(request.form.get("txtPrecio"))
        categoria = request.form.get("txtCategoria")

        m=Menu(nombre, descripcion,precio, categoria, True)
        db.session.add(m)
        db.session.commit()
        # redireccionas ruta
        #return redirect("sql_todos.html")
        # llamas a la función
        return redirect(url_for("sql_todos"))

        #puedo llamar a la función sql_todos¿?
     
    #es un GET - cuando cargas el formulario carga con un GET
    else:
        return render_template("form_anadircomida.html")


@app.route("/actualizar_comida", methods=["GET","POST"])                           
def actualizar_comida():  
    #captamos la información del formulario de forma basica "form"
    #AL DAR AL BOTON AÑADIR ESTAMOS UTILIZANDO EL "POST"
    men=Menu.query.get(id)
    if request.method== "POST":
       
        #2 formas diferentes de hacer el POST
        men.nombre = request.form.get("txtNombre")
        men.descripcion = request.form.get("txtDescripcion")
        men.precio = float(request.form.get("txtPrecio"))
        men.categoria = request.form.get("txtCategoria")

        db.session.add(men)
        db.session.commit()
        # redireccionas ruta
        #return redirect("sql_todos.html")
        # llamas a la función
        return redirect(url_for("sql_todos"))

        #puedo llamar a la función sql_todos¿?
     
    #es un GET - cuando cargas el formulario carga con un GET
    else:
        return render_template("form_actualizar.html",men=men)


@app.route("/borrar_comida", methods=["GET","POST"])                           
def borrar_comida():  
    #captamos la información del formulario de forma basica "form"
    #AL DAR AL BOTON AÑADIR ESTAMOS UTILIZANDO EL "POST"
    men=Menu.query.get(id)
    if request.method== "POST":
       
        #2 formas diferentes de hacer el POST
        men.nombre = request.form.get("txtNombre")
        men.descripcion = request.form.get("txtDescripcion")
        men.precio = float(request.form.get("txtPrecio"))
        men.categoria = request.form.get("txtCategoria")

        db.session.add(men)
        db.session.commit()
        # redireccionas ruta
        #return redirect("sql_todos.html")
        # llamas a la función
        return redirect(url_for("sql_todos"))

        #puedo llamar a la función sql_todos¿?
     
    #es un GET - cuando cargas el formulario carga con un GET
    else:
        return render_template("form_actualizar.html",men=men)

@app.route("/sql_todos")     
def sql_todos():     
    #mostrar todos los datos de la bd
     listamenu = Menu.query.all()
     #men = Menu.query.filter_by(activo=True) muestra los registros q no has borrado(false)
     return render_template("menu.html",menu=listamenu)
     #men = Menu.query.filter_by(nombre="Maria")
     #esto sería sin formulario. el jueves hicimos eso
     #s=""   
     #for p in men:
         #s =s+p.nombre
     #return s  

# no tiene asignada ninguna pagina web (html). es para cargar la bd inicial con los platos
#COMO NO FUNCIONA LA RELLENAMOS POR MEDIO DE FUNCIÓN

@app.route("/cargainicial")  
def  rellenar_primeravez():
     c1 = Menu("Rape","Rape a la parrilla", 45.98, "PESCADO", True)
     c2 = Menu("Rodaballo","Rodaballo a la parrilla", 98, "PESCADO",True)
     c3 = Menu("Merluza","Merluza, apionabo y menier (individual)", 25, "PESCADO",True)
     c4 = Menu("Entrecot", "CARNE", 28,"CARNE",True)
     #add all inserta una lista
     db.session.add_all ([c1, c2, c3, c4])
     db.session.commit()
     return "Carga inicial"

if __name__=="__main__":
    #rellenamos los datos por primera vez y luego no la volvemos a ejecutar
    #rellenar_primeravez() NO FUNCIONA ASI Q LA RELLENAMOS
    #para no tener que parar el servidor y volverlo a lanzar despues de realizar modificaciones
    #NO REINICIA con debug=False
    app.run(debug=False)
    #necesitamos un constructor en la clase menu "init"

