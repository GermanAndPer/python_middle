#Para abreviar la libreria podemos poner AS y el nombre a guardar
#PLT es la forma mas comun de guardar MATPLOTLIB
import matplotlib.pyplot as plt

def my_fist_barchart(labels, values):
  # Lo primero que necesitamos es darle la figura que realizaremos (Grafico)
  # Y sus Cordenadas
  #FIG y AX son sun nomenclaturas mas comunes
  #Mismo datos se llenarán con la Libreria

  #Estos cson codigos que siempre pondremos.
  #Tal cual no ponemos datos. 
  fig, ax = plt.subplots()
  #Ahora con AX nos va a ayudar a saber que Grafico haremos.
  #Aqui el de BARRAS
  # Y le damos los VAlORES LABELS y VALUES
  #Estos mismos valores se repiten mucho. Por eso se utilizan como ARGUMENTOS
  ax.bar(labels, values)
  #Y para imprimir el grafico, solo con el METODO PLT.SHOW()
  plt.show()


def my_fist_piechart(labels, values):
  fig, ax = plt.subplots()
  #Para el grafico de Pastel PIE
  #Algo peculiar es que para los labels en el PAY lo asignamos con =. 
  #Especialmente Importante si el argumento de labels se llamó diferente
  ax.pie(values, labels=labels)
  #Los siguientes argumentos son para que el grafico este en el centro
  #Y que sea un circulo.
  ax.axis('equal')
  #Y para imprimir el grafico, solo con el METODO PLT.SHOW()
  plt.show()


