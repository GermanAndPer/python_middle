#Se agregan condiciones en los ciclos y diccionartios
import random

name = ['German', 'Aaron', 'Rodrigo']
age= [28, 33, 23]

usuarios = {usuario: edad for (usuario, edad) in zip(name, age)}
print(usuarios)

#De esta manera agregamos condicionales
#RECODAR que las variables que iteran seran las que evaluamos.
users = {usuario: edad for (usuario, edad) in zip(name, age) if usuario != 'German'}
print(users)



#Para el siguiente caso aplicamos la condicion IF y IN
#Para que valide solo ciertos caracteres
texto = 'Hola mundo-Hello World'
vocales = {caracteres: caracteres.upper() for caracteres in texto if caracteres in 'aeiou'}
print(vocales)



#Tambien podemos hacerlo a la inversa
#Para este caso agregamos NOT para especificar que 
#Nos de todos los caracteres EXCEPTO ese.
texto = 'Hola mundo-Hello World'
vocales = {caracteres: caracteres.upper() for caracteres in texto if caracteres not in 'aeiou'}
print(vocales)


#Reto
#Contar cuantas veces apararece una letra en la cadena.
texto = 'Hola mundo-Hello World'
vocales = {caracteres: texto.count(caracteres) for caracteres in texto if caracteres in 'aeiou'}
print(vocales)