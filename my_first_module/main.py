# Los modulos son todos esos archvios que son .PY
# Y los llamamos con la palabra IMPORT
# Este es el ejemplo mas comun

import random
#Los modulos que llamamos por lo regular son solo funciones
#Esto nos ahorra codigo.
#Así solo indicamos los PARAMETROS para que funciones el MODULO
#Ejemplo

#Usamos una VARIABLE para guardar el VALOR.
#se llama poniendo el nombre de lo importado en este caso RANDOM
#Despues la funcion dentro del MODULO a UTILIZAR en este caso RANDINT
#como argumento solo pide el rango de numeros que necesitas para obtener el ENTERO
numero_aleatorio = random.randint(1,3)
print(numero_aleatorio)


# Nosotros podemos crear modulos.
# Junto a IMPORT ponemos el nombre del modulo a llamar Que es como se llama el archivo


import all_variations
all_variations.run()

'''
{
  'Original': 'Hello World', 
  'Mayusculas': 'HELLO WORLD', 
  'Minusculas': 'hello world', 
  'Nom Prop': 'Hello World'
}
'''