""" print("Hola")
# lista = ["jon", 45, 35.6666, "maria"]
# print(lista[1])
# lista.append("sahjsajhs")
# lista.insert(2, 4.55555)

# for i in lista:
#     print(f"Estoy pasando por la {i}")
#     print("Estoy pasando por la " + str(i))
# lista[1]=2
#  """
# compras = ["platanos", "manzanas", "leche"]
# compras.append("galletas")
# compras.insert(3,"zumo")

# for i in compras:
#     print(i)
# print(compras[1])
# print(compras[2])
# print(compras[-1])
# print(compras[-2])
# z=0
# for i in compras:
#     z=z+1
#     if i=="zumo": compras[z]="zumo de naranja"
# compras.pop()
# j=len(compras)
# z=int(j/2)
# compras.insert(z,"limones")
# compras.sort()
# for i in compras:
#     print(i)

""" alumnos=["Arturo","Jukio","Dani"]
a=input("cual es tu nombre")
Cantidad=0
for alumno in alumnos:
    respuesta=input(f"Ha venido {alumno} a clase? (y/n) ")
    if respuesta=="y": 
        Cantidad=Cantidad+1
print (f"{Cantidad}, alumno(s) están presentes hoy") """

alumnos=[]
MAX=10
for i in range(MAX):
    alumno=float( input("cual es tu nota?"))
    alumnos.append(alumno)
suma=0


for alumno in alumnos:
    suma=suma+alumno
   
print(f"La media de las notas es {suma/len(alumnos)}")
print(f"El valor máximo es {max(alumnos)}")
print(f"El valor máximo es {min(alumnos)}")
help("modules")