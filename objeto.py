#definiendo la clase
# class Persona:
#     #atributos
#     nombre =""
#     edad= 0
# #programa principal - estamos instanciando - usando
# jon = Persona()
# maite = Persona()
# print(jon.edad)
# jon.edad = 18
# print(jon.edad)
# maite.nombre = "Maite"
# print(maite.nombre)
class Persona:

#pasar la propia clase como primer atributo del constructor: self serian como los datos y los otro son atributos, sino no funciona
#en lugar de self puedes poner otro nombre
    def __init__(self, _nombre, _edad, vida=3):
        self.nombre = _nombre
        self.edad = _edad
        sel,vida = 3
        print("estoy vivo")
    def defender(self)
        self.vida = self.vida -1

    def hablar(self):
        #espera primer parametro objeto de la clase
        #los print no situarlos en los metodos o funciones
        nombre = self.upper()
        print (f"hola, soy  {nombre}")

jon = Persona("Jon", 18)
#get obtener valor
print(jon.nombre)
print(jon.edad)
# da información sobre los atributos y funciones¿?
print(dir(jon))
#set dar valor
jon.edad = 35 
print(jon.edad)
jon.hablar()
maria = Persona("Maria",40)
maria.hablar()

personas =[]

if __name__=="__main__":
    #si hay + de una persona bucle
    nombre = input("Introduce nombre usuario ")
    edad = input("Introduce edad ")
    persona1 = Persona(nombre, edad)
    #guardalo en la listamar
    personas.append(persona1)
    print(dir(personas))