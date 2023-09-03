import random

#Las Funciones nos ayudan a escribir codigo. 
#Y poder re utilizarlo tantas veces como sea necesario.
#Sin la necesidad de tener que escribir todo de nuevo.


#DEF
#La palabra recervada es DEF.
#para poder DEFINIR que es una variable.
#Despues le damos un nombre y la cerramos entre () y finalizamos con :
#Despues em su interior ponemos todo el codigo que vamos are utilizar.
def aleatorio():
  print('Voy a imprimir un valor aletario: ', random.randint(1,100))
#Y para llamar la funcion solo usamos su nombre y los parentesis.
aleatorio()



#Otra manera de hacerlos es dandole PARAMETROS a una funcion
#Al momento de que se define la funcion, ponemos los parametros que nesitaremos.
#Estos parametros son variable cullo valor se van a insertar dentro de la funcion Donde se especifica

#Por ejemplo, usaremos una llamada TEXT
# Y cuando llamemos la funcion, aquellas partes del codigo donde se pudo TEXT, será remplazada por lo que hayamos indicado
#Podemos poner N cantidad de Parametros

def mi_texto(texto):
  print('Aqui vamos a imprimir tu texto => ', texto)
#Tambieen se puede llamar una funcion dentro de otra funcion.
  aleatorio()

mi_texto('ESTO ES UN PARAMETRO')

