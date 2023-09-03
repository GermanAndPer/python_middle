#NAME SPACE
#NAME SPACES hace referencia a las palabras reservadas
#HAciendo referencia a palabras que yqa no puedes utilizxa 
#Por que ya hacen referencia a algo mas

#Importancian de paquetes}
#Usamos FROM para especificar la RUTA. y el nombre del MODULO a IMPORTAR
#Despues en IMPORT llamamos todas las funciones que vamos a llamar.

'''
from packages.mod_1 import func_1, func_2
#Si usamos * Como nombre de las FUNCIONES se important todas en el MODULO
from packages.mod_2 import *

print(func_1())
print(func_2())
print(func_3())
print(func_4())
'''


#Esta es una manera llamar la informacion
#Pero por Buenas practicas necesitamos usamos el archivo INIT
#    __init__.py

#Este es un archivo que en cuanto se crea, se ejecuta.
#Es por eso que lo que se ponga ahí, estará disponible en todo momento.
#Por el mismo motivo, las variables, estan disponibles para llamarlas.
#Si es que así se desea.
#lo unico que se necesita es dar el nombre del Paquete
import packages


print(packages.url)

#Por lo mismo que los comandos y datos de __init__ estan siempre activos, que desde ahí es donde se llaman los paquetes.
#Para no llamarlos en cada archivo.
#Y para que esten siempre disponibles.
#Pero eso hace que nuestro primer codigo no necesariamente funcione.
#Ahora debemos poner el origen de los archivos.
#Tal cual funciones
print(packages.func_1())
print(packages.func_2())
#Aunque funciona diciendo solo la funcion, podemos ser mas exactos 
#Y decir tambien el modulo
print(packages.mod_2.func_3())
print(packages.mod_2.func_4())