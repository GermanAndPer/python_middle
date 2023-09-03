#LAMBDA
#LAMBDA o FUNCIONES ANONIMAS
#Es una forma diferente de escribir funciones.
#Es una maner simplificada

#Esta es la manera Normal
def mi_nombre(nombre, apellido):
  return f'Mi nombre es {nombre} {apellido}'

nombre = mi_nombre('German','Andres')
print(nombre)



#Esta es la version LAMBDA
#DEF es cambiado por LAMBDA
#El nombre de la variable ahora va al principio
#Puedes poner tantos argumentos como necesites pero ya no necesitan ()
#y RETURN cambia a dos puntos :
nombre_v2 = lambda nombre, apellido : f'Mi nombre es {nombre} {apellido}'
#Y al momento de llamarlas se hace igual que con una funcion normal
#Indicando todos sus parametros
print(nombre_v2('German','Andres'))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(11))