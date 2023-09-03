#Normal
#Podemos iterar un siclo dentro de una lista.
#De la siguiene mamera
#Primero necesitamos un diccionario donde pondremos los datos.
import random

#Para este caso, usamos element para iterar y para para asignar la CLAVE 
#Y random para asignar el VALOR.

dir_v1 = {}
for element in range(1,11):
  dir_v1[element] = random.randint(1,100)

print(dir_v1)

#Lista
#Tambien se pueden juntar listas a un diccionario.
name = ['German', 'Aaron', 'Rodrigo']
age= [28, 33, 23]
print(type(age))
#Una manera de combinar 2 o mas Valores en con ZIP
#Y pones entre los los parentesis del METODO las listas a unir
#pero se se hace solo esto, se imprime un Hash.
print(zip(name,age))
#Para eso agregamos lista, pero lo curioso es que las convierte en tuplas
#Pero en realidad creo una lista con tuplas.
print(list(zip(name,age)))

#Para poner un juntar los valores, es necesario usar ZIP al mencionar las listas que se llamaron
#No olvidar el punto y como para separar las variables que iteran
usuarios = {usuario: edad for (usuario, edad) in zip(name, age)}
print(usuarios)