#Dentro de OPEN y Depsues de escribir la direccion del archivo
#esta "R"
#este hace referencia a solo lectura (READ).
#Si lo cambiamos a "W", seria de solo escribir(WRITE).
#Lo cual tampoco es UTIL
'''
with open('./27_txt.txt', "r", encoding="UTF-8") as file:
  for line in file:
    print(line)
'''
#pero si ponemos "R+"
#ahora sí serian pérmisos de lectura y escritura
#Y cada que escribamos algo se va a poner al final
with open('./27_txt.txt', "r+", encoding="UTF-8") as file:
  for line in file:
    print(line)
  #para escribir se usa el METODO WRITE
  #Se recomienda poner "\n" para que se escriba en una nueva linea.
  # encaso de no ponerla, se agregará a la ultima linea.
  # pero no generará nuevas.
  file.write("\nEsta será una line a nueva.")

#----------IMPORTANTE----------
#en caso se escrivir W+ en vez de R+, sse borrará todo cada que se ejecute
#