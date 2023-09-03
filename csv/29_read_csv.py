import csv
#Es un modulo especial para leer CSV


#Lo primero que se necesita es crear la funcion que abrirá el CSV
#para este caso, dejamos la ruta como parametro de la funcion
def read_csv(path):
  #Despues ponemos el clasico codigo que abrirá el archivo y le pendrá una referencia para usos futuros
  #Ponemos "R" por que solo queremos visulizar,
  with open(path,'r') as csvfile:
    #Antes de crear el ciclo, necesitamos una variable donde vamos a poner las caracteristicas del archivo
    #Lo primero que haremos, será llamar al el MODULO CSV
    #Y usar las funcion READER
    #Lo primero que pide es la VARIABLE del archivo con la RUTA
    #Para este caso CSVFILE
    #Despues el Delimitador--Por lo regular es un coma ,
    #Pero poner lo que corresponda
    lectura = csv.reader(csvfile,delimiter=',')
    #El objetivo final es tener un DICCIONARIO con las poblaciones Mundiuales
    #Para eso vamos a necesitar 2 cosas.
    #1-- Los encabezados. Pues los vamos a necesitar para cada linea,
    #Será de la misma manera que cuando leimos un TXT.
    #Pero esta vez no imprimimos. MAs bien guardamos el valor en una VARIABLE
    header = next(lectura)
    # Y un diccionario vacio donde pondremos los datos
    data = []
    #una vez que ya tengamos esto podemos hacer el FOR
    #El For es para que lea cada una de las Lineas y la imprima.
    for row in lectura:
      #Antes de imprimir necesitamos generar una variable que tenga los datos
      #CLAVE: VALOR
      #importante usar ZIP para que no queden como tuplas.
      iterable = zip(header, row)
      #ahora para armar la fila completa, usamos
      #DICTIONARY COMPRENTION
      country_dictionary = {key: value for key, value in iterable}
      #Ahora que tenemos la linea completa no solo la queremos ahí.
      #Debemos guardarla en algun lugar. El Diccionario que creamos.
      #para eso usamos append
      data.append(country_dictionary)
      #una vez terminado, solo Retornamos el Dictionary
    return data
   
    #Esto imprime cada linea como lista.

if __name__ == '__main__':
  #No solo ejecutamos la Funcoion
  #Como nos va a devolver un valor lo guardamos en uan variable.
  data = read_csv('./csv/data.csv')
  #Al final solo imprimimos.
  print(data[0])
  