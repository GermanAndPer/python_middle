# List Comprehension
# Es como combinar un ciclo FOR y una lista.
# Esto con la finalidad de acortar coodigo.
# Esto a su vez, ayuda a que sea mas legible.

#Esta es la forma normal.

numbers = []

for element in range(1,11):
  numbers.append(element)

print(numbers)

#Esta es la manera simplicada
#Todo se hace desde la creacion de la lista
numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)
#Tambien se pueden aplicar operaciones
numbers_v3 = [element * 2 for element in range(1,11)]
print(numbers_v3)

#CONDICIONAL
#Ademas de aplicar FOR tambien podemos aplicar condicionales como IF

#EJEMPLO de solo numeros pares

numbers_v4 = [element for element in range(1,41) if element % 2 == 0]
print(numbers_v4)
# se pueden agregar mas operadores
