#para maenar errores usamos TRY CATCH
#Pero aqui es llamada #TRY EXCEPT
#Para poder ejecuitarlos, se necesitan importar los PAQUETES RE
#RE - Espresiones Regulares
#Mas especificamente el Modulo de Errores - ERROR

from re import error


#para empezar pones  TRY:
#Despues el codigo que queremos ejecurar.
try:
  print(0/0)
#Despues de eso EXCEPT y el error como aparece en consola.
#Este error puede variar, y dependiendo de este mismo, decidimos que ejecutar
#Adicional a eso ponemos AS ERROR(error solo es un ejemplo-Puede se lo que sea):
#este ERROR será la decripcion en Automatico dada por el el sistema
#En dado caso de que queramos guardar esa informacion en algo en especifico.
#Aqui solo se imprime
except ZeroDivisionError as error:
  print(error)
except ValueError as error:
  print(error)
#Podemos poner tantas Excepciones como creamos necesarias

#assert 1 != 1, "El 1 no es diferente de 1"
#Los errores podrian ser guardados en un reporte de errores para saber donde esta el problema

