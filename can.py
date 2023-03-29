class can:
      
    def __init__(self, nombre, raza, edad, dueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.dueño = dueño

    def comer(self):
        print(f"{self.nombre} Está hambrient@ ")

    def dormir(self):
        print(f"{self.nombre} Está durmiendo ")

    def ladrar(self):
        #podemos jugar con los atributos
        if self.edad<10:
            print(f"{self.nombre} Está ladrando ".upper())
        else:
            print(f"{self.nombre} Está ladrando ")

    def mostrar(self):
        print(f"{self.nombre} tiene {self.edad} años {self.raza}")

#sobreesecribir la función str q viene por defecto
    def _str_(self):
        return "hola dundee function"
#comparo solo la edad    
    def _eq_(self,otro):
         return self.edad==otro.edad
    
num = 0
cans =[]
if __name__=="__main__":
        miles=can("Miles",4,"Jack")
        lupe =can("lupe",5,"gatuna")  
        ok =can("ok",7,"golden") 
        # el perro tiene varios dueños - creas la tupla y asignas valores 
        miles=can("miles", 12, "bulldos, ["xabi","carmen"]")
        #funciones q vienen con la clase. tengo el control sobre ellos al poder modificar a nuestro gusto: dundee function   
        print(dir(lupe))
        cans.append(miles)
        cans.append(lupe)
        cans.append(ok)

        #miles==lupe se puede comparar
        # while num<=3:
        #    nombre = input("Introduce nombre ")
        #    edad = input("edad ")
        #    raza = input("raza ")
        #    c1 = can (nombre, raza, edad)
        #    cans.append(c1)
        #    num +=1
        # for c in cans:
        #    # c.mostrar()
        #     #print(c.nombre, c.edad, c.raza)
        #     print(c)
        for c in cans:
             print(c)
             print(c.nombre, c.edad, c.raza)