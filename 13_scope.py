#GLOBAL
#Variable que se crea de manera general
explicacion = 'Esto es una variable GLOBAL'


#LOCAL
#Por ejemplo, esa que se crea dentro de una FUNCION
#En caso de crear un variable con el mismo nombre que una GLOBAL
#Esta se tomará como nueva Y funcionará como si se acabará de crear
def variable_local():
  explicacion = 'Esto es una variable LOCAL'
  otra_explicacion = 'Son variables locales las que estan dentro de una FUNCION'
  print(otra_explicacion)
  return explicacion


print(explicacion)
resultado_funcion = variable_local()
print(resultado_funcion)
#Ver que no estemos llamando una variable con un contexto definido
#Por tanto, si llamamos variable que estan dentro de una funcion
#Pero estemos fuera de esta, dará error
print(otra_explicacion)
