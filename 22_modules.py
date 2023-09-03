import sys
#Es para cosas relacionadas con el sistema
#Esto nos dice la localizacion del archivo utilizado
print(sys.path) 



import re
#Por EXPRESIONES REGULARES
#Como su nombre lo dice, son formas regulares de especificar algo
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
#Aqui lo que queremos hacer es obtener ciertos valores
#Para eso es FINDEALL
#Entre comillas ponemos que vamos a buscar.
#[0-9] es para buscar numeros del 0 al 9
#para [0-9] ver EXPRESIONES REGULARES
#El + es para encontrar mas de 1 coincidencia
#y al final la variable con los datos a validar
result = re.findall('[0-9]+',text)
print(result)



import time
#Esta es para importar dartos de tiempo.
#TIME.TIME() - llama la hora actual, por en segundos.
timestamp = time.time()
print(timestamp)

#Para ver el lenguaje humano necesitamos 2 llamar 2 METODOS.
#Esto trae la hora local
local = time.localtime()
#Pero para que sea en lenguaje humano, usamos ASCTIME
#HAce referencia al codifo ASCII
ahora = time.asctime(local)
print(ahora)




import collections
#Tieme varios fines.
#El Metodo COUNTER Sirve para hacer un diccionario
#En este diccionario, lee una lista,
#Y te devuelve los ITEMS de la lista y Cuantas veces se repiten
#Estos como CLAVE-VALOR respectivamente
numbers = [1,1,2,1,2,1,4,5,3,3,21]
#Usamos el metodo Counter
#IMPORTANTE--Inicia con C mayuscula
contador = collections.Counter(numbers)
print(contador)