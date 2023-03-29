from flask import Flask,render_template,redirect,url_for, request
from flask_sqlalchemy import *
import os

app=Flask(__name__)

#RUTA
basedir = os.path.abspath(os.path.dirname(__file__))
#dobnde va a colgar la bd sqlite y la bd se llama database.db
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
#iniciamos
#db.init_app(app)
# hereda de la clase Base definida con ORM gestiona b.d - metodos y atributos q nos permite guardar en una b.d 
#definimos la tabla. Hay q declarar

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250), nullable=False)

@app.route("/")    
# es el insert
def Index():
    jon=Persona()
    jon.nombre = 'Jon'
    db.session.add(jon)
    db.session.commit()
    return "hola"

""" with app.app_context():
    db.create_all() """
#declaracion de ruta principal
@app.route("/")
def index():
    return "hola"

@app.route("/sql_delete")
#seleccionar a la persona antes de borrarla. pasamos el objeto en su globalidad
def sql_delete():
     persona= Persona.query.get(5)
     db.session.delete(persona)
     db.session.commit()
     #return "no lo encuentra"
     #personas contiene una lista de objetos Persona
     personas=Persona.query.all()
     #para mostrar los datos de esa lista hacemos un 'FOR?
     s=""
     for p in personas:
         s=s + " " +p.nombre
     return s



@app.route("/sql_update")     
def sql_update():     
    #update en sql - iria en otra función
     persona = Persona.query.get(5)
     persona.nombre = "Jonathan"
     db.session.add(persona)
     db.session.commit()

     s = persona.nombre
     return s

if __name__=="__main__":
    #para no tener que parar el servidor y volverlo a lanzar despues de realizar modificaciones
    app.run(debug=True)