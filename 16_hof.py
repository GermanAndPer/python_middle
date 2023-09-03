#HOF
#HIGH ORDER FUNTIONS
#Se les llama así cuando se tiene Funciones que llaman otras Funciones



#Esta es la manera trradicional
def suma(x):
  return x + 1
print(suma(1))


def multiplicacion(x, func):  #FUNC es para especificar la FUNCION
  return x * func(x)          #y aqui especificamos los ARGUMENTOS
#Aqui llamamos la funcion HOF que llama a la otra FUNCION
#como vamos a llamar otra funcion, esta no requiere parametros
#Los mismos parametros de la Funcion Interna esta en la FUNCION HOF
print(multiplicacion(3, suma)) 



#Se puede simplificar de la siguiente Manera
#Usando LAMDA
#Lo que optimizamos es la funcion que llama la otra funcion
#Esto debe de dar el mismo resultado
result_suma = lambda x: x +1
print(multiplicacion(3, result_suma)) 


#Ahora, esto se puede simplificar aun mas
#Podemos hacerlo desde el PRINT
#En lugar de llamar la funcion CREARLA con LAMBDA
#Y nos da el mismo resultado
print(multiplicacion(3, lambda x: x +1)) 


#La versatilidad  de esta manera, es que nisiguiera tenemos que gurdarla
#Podemos agregar datos al mismo momento de llamarlos.
#Lo que hace que podamos modificarlos como queramos.
print(multiplicacion(3, lambda x: x +1)) 
print(multiplicacion(3, lambda x: x -1)) 
print(multiplicacion(3, lambda x: x *1)) 