#LOOPS
#Esta es la forma mas comun
#La manera predeterminada

for element in range(1, 11):
  print(element)

#Que si asigmanos ese valor a una variable no significa nada
#Unicamente un STRING mas
iteracion = range(1,11)
print(iteracion)

#Tentonces necesitamos darle un usar una FUNCION ITER
#Sin embargo esto solo nos genera los valores indicados
#Pero nos los genera como un Objeto
iteracion = iter(range(1,11))
print(iteracion)

#A pesar de esto, podemos evaluar la informacion uno por uno
#Para eso usamos NEXT
print(next(iteracion))
#Y podemos iterar tantas veces como sea necesario
print(next(iteracion))
print(next(iteracion))
#Por cada vez que se haga se dará un salto.
print(next(iteracion)) 
#En caso de poder mas de los ITEMS existente, se va a indicar que no existe



# O en caso de querer el rango de un objeto en otros datos mas legibles 
# lo podemos trasnsformar
# Podemos usar funciones como LIST, TUPLE o SET
iteracion = list(iter(range(1,11)))
print(iteracion)
