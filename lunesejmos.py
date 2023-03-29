import os
import platform #pq no funciona el os.uname

print("estoy ejecutando el programa")
print(platform.uname())
print(os.name)

print(os.getcwd())
path= os.path.join(os.getcwd(),"carpeta")
print(path)
print(os.path.split(os.getcwd()))

patch= os.path.split(os.getcwd())
print(patch[0],patch[1])

#s= os.listdir(path) da error pq no está creada la "carpeta" y entonces el sistema no encuentra la ruta especificada
s= os.listdir(os.getcwd())
print(s)

print(os.path.isfile(os.path.join(os.getcwd(),"abc.py")))
