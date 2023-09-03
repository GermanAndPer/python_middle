#MAP
#Es las convercion de Listas en otras diferentes
#Es de las FUNCIONES mas comunes
#En si, lo que hace MAP es que nos devuelve un valores individuales
#Pero estos pueden convertirse en LIST, TUPLE dependiendo lo que se necesite



#Esta es la forma con LOOPS
#Para este caso, necesitamos la una lista con valores
#Y otra pero sin valores, que pondremos los datos ITERADOS
lista_1 = [1, 2, 3, 4]
lista_2 = []

for element in lista_1:
  lista_2.append(element * 2)

print(lista_1)
print(lista_2)



#La siguiente es una la misma forma, pero aplicando LAMBDA
#Ademas usamos tambien MAP
#una vez que tengamos la funcion usamos MAP para que extraiga cada uno de los valores
#despues agregamos LIST, para que los valores se agreguen como LIST
#Esta es una estructura en la que podemos hacer un LOOP
#Sobre cada uno de los elementos

lista_3 = list(map(lambda element: element * 2, lista_1))
print(lista_3)

#Tambien podemos convertir los elementos en una TUPLA
lista_3 = tuple(map(lambda element: element * 2, lista_1))
print(lista_3)



#Tambien podemos iterar 2 LISTAS
numeros_1 = [1,2,3,4]
numeros_2 = [5,6,7]
#Necesitamos una tercera en la que pondremos los valores que necesitamos
numeros_3 = list(map(lambda num1, num2: num1 * num2, numeros_1, numeros_2))
#las lsita que sale en este caso, es el resultado de multimplicar
#el primer numero de la lista uno por el primero de la segunda.
#Luego el segundo por el segundo, etc.
#Pero solo vamos a optener el valor de los ITEMS que puedan ITERAR
#En caso que no haya cruce, se omiten
#Por eso al final la lista solo tiene 3 VALORES
print(numeros_3)



