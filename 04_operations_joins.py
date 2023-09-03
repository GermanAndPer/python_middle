#las Operaciones son lo que se conoce como JOINS en SQL
#Y para ello se necesitasn SETs

set_a = {'Mexico','Japon','Rusia', 'Colombia'}
set_b = {'Canada', 'Colombia', 'Chile','Mexico'}
print(set_a)
print(set_b)

# UNION
# El METODO UNION hace referencia a al FULL OUTER JOIN
# Une ambos SETS y los trata como si fueran uno solo. 
# Eso incluye eliminar duplicados.
set_c = set_a.union(set_b)
print(set_c)
# | 
#Tambien se puede usando el operador | 
# Y se obtiene el mismo resultado.
print(set_a | set_b)





# INTERSECCION
# El METODO INTERSECCION hace referencia a al INNER JOIN
# Muestra solo los elementos que aparecen en ambos SET. 
set_c = set_a.intersection(set_b)
print(set_c)
# &
# Para remplazar el metodo usamos el Operador & 
print(set_a & set_b)






# DIFFERENCE
# Hace el efecto del LEFT JOIN. 
# Quitando todas los elementos que aparecen en el SET B
set_c = set_a.difference(set_b)
print(set_c)
# -
# Para remplazar el metodo usamos el Operador -
print(set_a - set_b)





# SYMMETRIC DIFFERENCE
# Para este METODO usamos SYMMETRIC DIFFERENCE 
# hace referencia al FULL OUTER JOIN
# PEro para este caso, elimina las intesecciones. 
# Y deja las restantes.
set_c = set_a.symmetric_difference(set_b)
print(set_c)
# ^
# Para remplazar el metodo usamos el Operador ^
print(set_a ^ set_b)
