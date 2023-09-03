#SET
#Similar a los diccionarios.
#{}
set_contries = {'Mexico','Japon','Rusia'}
print(set_contries)
print(type(set_contries))


#En caso de haber datos repetidos, estos se eliminan y se quedan solo 1
#Al momento de imprimir, puede hacerlo de forma aleatoria. 

set_contries = {'Mexico','Japon','Rusia','Mexico'}
print(set_contries)
print(type(set_contries))

#Lo mismo aplica para los numeros

set_numeros = {1, 2,4,6,78,89,0,2,2,3}
print(set_numeros)
#Observar que para el caso de los numeros, sí los acomoda. 


#Tambien acepta varios tipos.
set_random = {1, 2, 3, False, 'Hola', 'Adios'}
print(set_random)

#Las anteriores fueron maneras EXPLISITAS de generar un SET.
#Esta es la manera INPLISITA

string_random = 'Hola mundo'
string_to_text = set(string_random)
print(string_to_text)
#Combierte cada uno de los caracteres en un elemento del SET.

#De una manera similar, pero tomando todos sus valores, podemos convertir; 
#LISTAS, TUPLAS a SET
mi_lista = ['Jamon', 'Pan', 'Cebolla', 'Leche', 'Pan']
list_to_text = set(mi_lista)
print(list_to_text)

mi_tupla = ('a', 'b', 'c', 'c')
tuple_to_text = set(mi_tupla)
print(tuple_to_text)
print(len(tuple_to_text))

#Si al final lo que se quiere obtener de ello es una lista, aplicamos la conversion implicita

list_v2  = list(list_to_text)
print(list_v2)