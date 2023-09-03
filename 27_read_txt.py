#Estas son las maneras en la que podemos leer un archivo
#OPEN
#Usamos OPEN para almacenar la ruta de un archivo a recibir.
#mismo que despues servirá para leerlo.

file = open('./27_txt.txt')
#Y para ver su conteido usamos el metodo .READ
#Ademas de PRINT
print(file.read())
#Pero si hacemos esto debemos usa .CLOSE para cerrar el archivo.
#Pues si lo dejamos ABIERTO, va a consumir espacio en memoria
#Lo cual, si el archivo es muy pesado, puede ser perjudicial
file.close()

#Otra manera de leer el archivo sin, afectar negativamente la memoria
#Es con .READLINE
file = open('./27_txt.txt')
print(file.readline())
#Y por cada vez que pongamos este codigo, se imprimirá una nueva linea.
print(file.readline())
print(file.readline())
#El unico problema con esto es que no sabemos cuando teminar de imprimir
#Por lo que no sabemos cuantas veces repetir la linea.


#Para estos caso mejor usamos FOR y leer la linea
#Esto lee cada una de las lineas Pero al final se tiene que cerrar..
for line in file:
  print(line)
file.close()


#el ultimo ejemplo, y el como se enocntrará normalmente en la vida laboral
#Es con WIYH
#Y con esta manera ya no será necesario cerrar el archivo al finalizar.
#Lo hará automaticamente

with open('./27_txt.txt') as file:
  for line in file:
    print(line)


#Podemos agregar una variable para agregar el enconding UTF-8
with open('./27_txt.txt', "r", encoding="UTF-8") as file:
  for line in file:
    print(line)
#En cierta instancia esto es opcional