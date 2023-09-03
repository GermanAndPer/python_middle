#Hay varias maneras de Validar si existe o no un error.
#El metodo mas simple es 
#ASSERT
#Solo escibimos ASSERT y el codigo a evalurar.
#Si tod esta bien, no aparecerá nada.
#En dado caso de que sí, se señalará

assert 1/1


#Ahora, que pasa si suseda algo que no queramos pero no necesariamente da un error
#Nosotros podemos propiciar el mensaje de error
#Con RAISE y EXCEPTION
# Ademas de marcar un error, podemso especificar un mensaje a aparecer
try:
  age = int(input('¿Que edad tienes? '))
  if age >= 18:
    print('Excelente, eres bienvenido.')
  elif age < 18:
     print('Acceso denegado. Solo mayores de edad.')
  else:
    print('Datos invalidos. Ingresa correctos.')
except ValueError as error:
  print('Lo siento esos noson datos validos')