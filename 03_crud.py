set_contries = {'Mexico','Japon','Rusia'}
print(set_contries)
print(len(set_contries))
print(type(set_contries))

#Para saber si un valor esta en tenemos un elemento dentro de una lista
#usamos IN
#Ponemos el valor a buscar, luego IN y al final el nombre del SET
print('Mexico' in set_contries)

#ADD
#Para agregar un Valor, usamos -EL METODO ADD
set_contries.add('Londres')
print(set_contries)

#UPDATE
#Una manera de agregar subconjuntos es con UPDATE
set_contries.update({'Canada', 'Colombia', 'Chile'})
print(set_contries)

#SORTED
#Para imprimirlo en Orden alfavetico, usamos SORTED
print(sorted(set_contries))

#REMOVE
#Una forma de eliminar elementos de los conjuntos es con REMOVE
#Solamente debemos llamar la funcion y el valor a eliminar
set_contries.remove('Londres')
print(set_contries)
#Solo que si vamos a elimnar un valor que no existe, genera error.
#Para evitar ese error, mejor usamos DISCART

#DISCART
#Discart Funciona exactamante igual que REMOVE
#Pero en caso de no existir el valor, continua con la ejecuccion.
set_contries.add('Chile')
print(set_contries)

#CLEAR
#Elimina todos los elementos en el SET.
set_contries.clear()
print(set_contries)
#Esto nos devuelve un SET Vacio.
