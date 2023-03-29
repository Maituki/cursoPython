#CLASE SUPER - PADRE
class Instrumento:
    def __init__(self, nombre, tipo, precio):
        self.nombre= nombre
        self.tipo= tipo
        self.precio= precio
        #privada
        self.__precio_coste = precio - 20

    def tocar(self):
        print(f"{self.nombre} esta tocando")

#diferentes caracteristicas de instrumentos segun el tipo: aire, etc. Piano hereda las cosas de instrumeto. HERENCIA PADRE-HIJO
class Piano(Instrumento):
    def __init__(self, nombre, tipo, precio, teclas, musico):
        #para acceder al padre ó madre poner SUPER
        super().__init__(nombre, tipo, precio)
        #añado valor a las variables especificas al HIJO
        self.teclas= teclas
        self.musico= musico
    #modificando el valor de los atributos. Funciona incluso poniendo otro parametro "a"
    def tocar(self):
        #print("ding ding ding")
        print(f"{self.musico.nombre} esta tocando...ding ding ding")

class Oboe(Instrumento):
    def __init__(self, nombre, tipo, precio, pulsador):
        #para acceder al padre ó madre poner SUPER
        super().__init__(nombre, tipo, precio)
        #añado valor a las variables especificas al HIJO
        self.pulsador= pulsador
    #modificando el valor de los atributos. Funciona incluso poniendo otro parametro "a" `pero cuando llamas a la funcion pasar otro parametro`
    def tocar(self,a):
        print("Banda sonora La Misión")   
class Musico:
     def __init__(self, nombre):
         self.nombre=nombre
        
if __name__=="__main__":
    #lista de musicos
    musicos=[]
    jon = Musico("jon")
    guitarra = Instrumento ("guitarra", "cuerdas", 100)
    guitarra.tocar()
    piano1= Piano("piano x", "cuerdas-percusión", 200, 50, jon)
    print(piano1.teclas)
    piano1.tocar()
    obo= Oboe("piano x", "cuerdas-percusión", 200, 50)
    print(obo.pulsador)
    #"caracter ó 1 numero"
    obo.tocar("e")
    #relacion de asociación - relacionar un objeto con otro
   