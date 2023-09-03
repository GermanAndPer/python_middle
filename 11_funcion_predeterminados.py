#Multiples resultados y Valores preddeterminados
#En dado caso de que el una funcion requiera varios parametros
#Pero no se indique ninguno, va a dar error
#Para eso damos un VALOR PREDETERMINADO

#Al momento de crear la funcion, e indicar los parametros usamos =
#el = mas su valor por defecto

def operaciones(value1=1,value2=2,value3=3):
  suma = value1 + value2 + value3
  multiplicacion = value1 * value2 * value3
  resta = value1 - value2 - value3
#En caso de revolver mas de un valor es necesario se PUEDE
# Usando Return y cada uno de los valores por coma
  return suma, multiplicacion, resta

#Si llamamos la funcion, y hay varios retornos nos devuelve una TUPLA
resultados = operaciones()
print(resultados)


#En caso de querer solo un resultado, podemos hacerlo de 2 formas
#1
#Llamando el resultado por su posicio
resultado_suma = operaciones()
#una vez hecha la Tupla, solo elegimos la posicion 
print(resultado_suma[0])

#2
#La segunda manera es creando las variables para cada posicion

total_suma, total_multi, total_resta = operaciones()
print(total_suma)
print(total_multi)
print(total_resta)




#Esta es la manera normal de asignar los argumentos que se van a dar
resultado_v2 = operaciones(10,20,30)
print(resultado_v2)


#Pero podemos elegir el valor exacto de un argumento
#Como si asignaramos un valor a una variable
#el nombre que se le dio el = y su valor.

resultado_v3 = operaciones(value2=10)
print(resultado_v3)