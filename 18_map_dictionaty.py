items = [
  {
  'product':'camisa',
  'price': 100
  },
  {
  'product':'playera',
  'price': 200
  },
  {
  'product':'pantalon',
  'price': 300
  }
]


#Esta es una manera de ver datos especificos de un Diccionario
#Especificamos la clave y el diccionario para saber que valor.
prices = list(map(lambda item: item['price'], items)) 
print(prices)

#Y esta es una manera de Excribirlo
#Para calculos mas complejos, no se recomienda LAMBDA
#Se recomienda mejor usar FUNCIONES normales

def taxes(item):
  item['taxes'] = item['price'] * .16
  return item

#Aqui solo mencionamos la funcion y su parametro
#Que termina ciendo el DICCIONARIO que se va a iterar.
new_products = list(map(taxes, items))
print(new_products)
#CUIDADO al EJECUTAR
#Pues esto puede que cambie el valor original
#Y puede que eso no sea lo que se quiera
print(items)


