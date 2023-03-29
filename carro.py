class coche:
          
    def __init__(self, marca, modelo, tipo_combustible, máximacapacidad_deposito, nivel_deposito):
        self.tipo_combustible = tipo_combustible
        self.marca = marca
        self.modelo = modelo
        self.nivel_deposito = nivel_deposito
        #valores por defecto
        #encapsulación
        self.__máximacapacidad_deposito = máximacapacidad_deposito
        # nadie puede ver el salario
        self.__salario=2000
        self.__deposito_actual = 12

        #self.máximacapacidad_deposito = 30
        #mínima cantidad cuando compras el coche
        #self.nivel_deposito=1
        #coche no averiado y con gasolina
        self.averiado=False
#asigno valor y valido    
    def set_tipo(self,tipo):
            if tipo not in ("diesel","gasolina","electrico"):
                  return None
            else:
                  self.tipo = tipo
    def get_tipo(self):
       return self.tipo_combustible

    @property
    # get - print
    def deposito_maximo(self):
          return self.__máximacapacidad_deposito
    #set - doy nuevo valor a la variable
    @deposito_maximo.setter
    def deposito_maximo(self, valor):
          if valor< 500:
                self.__máximacapacidad_deposito=valor
    
    # El desarrollador solo puede acceder a esta función y quitar 10 al salario (__ doble guión)
    def calcular_salario(self):
          return self.__salario -10 
    
    def calcular_salario(self):
          return self.__calcular_salario_subido(self)
    
    def __calcular_salario_subido(self):
          return 10000*12/1
    
    def conducir(self):
        if self.averiado == True:
            print("no puedes conducir. Esta averiado")
        else:
            self.nivel_deposito= self.nivel_deposito -5
            print(f"valor del deposito {self.nivel_deposito}")
            if  self.nivel_deposito>0:
                  print("estoy conduciendo")
                  print(f"Carga de depósito actual {self.nivel_deposito}")
            else:
                  print("No te queda combustible")
          
    def actualizar_deposito(self, nivel):
         if nivel<=self.fuel_maximo:
              self.__deposito_actual = nivel
              
    def llenar_deposito(self,cargasolicitada):
          if (self.nivel_deposito+cargasolicitada)>  self.__máximacapacidad_deposito:
               print("No es posible realizar la carga por exceso de combustible")
          print("cargar el depósito")
    
    def chocar():
          print("golpe tremendo")
          self.averiado = True
    def accidente(self, otro):
        #pierdes combustible
        self.nivel_deposito=-5
        otro.nivel_deposito=-5
# no hace falta funcion averiado pq tengo definido una propiedad - lo realizo
      #def averiado():
       #   print("golpe tremendo")
       

if __name__=="__main__":
        rav4= coche("Toyota","rav4","hidrogeno",100, 25)
        ford= coche("FORD","fiesta","electrico",200,40)
        #dato privado pero no lo es 100%. Forma de mirar el valor por defecto
        print(rav4._coche__máximacapacidad_deposito)
        print(rav4.nivel_deposito)
        print(rav4.get_tipo())
        print(rav4.set_tipo("diesel"))
        rav4.conducir()
        rav4.conducir()
        rav4.conducir()
        rav4.accidente(ford)
        #hacer property para acceder al contenido variable privada
        if rav4.nivel_deposito<5:
             print("Piloto combustible encendido.Repostar combustible")
             rav4.llenar_deposito(300)
        #print(ford.actualizar_deposito)
        print(rav4.deposito_maximo)
