from os import write
#primer paso leer todo el fichero
with open("sherlock.txt","r") as f:
  s = f.read()
  print(s)
#segundo paso - realizar la busqueda o las operaciones con la nueva variable "S" q tiene el contenido del fichero original
#cambiar s a mayuscula upper
s = s.upper()
print(s)
#tercer paso - crear nuevo fichero con las nuevas modificaciones
with open("resultado.txt","w") as f:
   f.write(s)
# #utilizar otras funciones - leer linea a linea
# with open("sherlock.txt","r") as f:
#   s1=f.readline()
#   s2=f.readline()
#   s3=f.readline()
#   print(s1,s2,s3)
# # leer todo el fichero pero miro por linea si existe la palabra "Hola"
#  with open("sherlock.txt","r") as f:
#     for line in f.readlines():
#         if "Hola" in line:
#             print(line) 


# guardamos y escribimos "s" en nuevo archivo
#abrimos archivonpara write
#write(s)