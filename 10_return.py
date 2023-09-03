#Por Default las funciones solo resuelve sus procedimientos durante la misma funcion
#Y los datos generados ahí no se pueden volver a utilizar.
#Para esos casos se utiliza:
#RETURN
#Retun permite que el valor obtenido se pueda utilizar Para procesos adicionales.



#Necesitamos una variable donde pondremos el resultado de la FUNCION 
def suma(a, b):
  sumatoria = a + b
  return sumatoria #Usamos return y la variable que tendrá el valor que usaremos por fuera
#Podemos obtener el valor con un PRINT
#Pero dentro llamamos la FUNCION y sus PARAMETROS
print(suma(1, 2))


#O podemos guardar su valor en una variable Externa
resultado = suma(3,4)
print(resultado)

#Si hacemos esto, podemos llamar su valor para afectarse a sí mismo en futuras referencias.

resultado_v1 = suma(resultado, resultado *2)
print(resultado_v1)