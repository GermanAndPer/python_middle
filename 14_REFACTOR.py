import random
def asignacion(eleccion_jugador):
  eleccion_jugador = armas[eleccion_jugador]
  print('Excelente elegiste ', eleccion_jugador)
  return eleccion_jugador

def asignacion_enemiga():
  eleccion_maquina = random.choice(armas)
  return eleccion_maquina

armas = ('Piedra 🪨', 'Papel 📃', 'Tijeras ✂️')
print('Vamos a jugar Piedra papel o Tijeras. \n El primero en perder sus 3 vidas, pierde. ♥️♥️♥️ \n 🪨 📃 ✂️ Elige tu arma 🪨 📃 ✂️', '\n','⬇️' * 20 )
vidas_jugador = 3
vidas_enemigo = 3

while vidas_jugador > 0 or vidas_enemigo > 0:
  eleccion_jugador = int(input('Indica el numero de tu eleccion 1-Piedra 2-Papel 3 Tijeras: '))-1
  if eleccion_jugador == 0:
    mi_eleccion = asignacion(eleccion_jugador)
  elif eleccion_jugador == 1:
    mi_eleccion = asignacion(eleccion_jugador)
  elif eleccion_jugador == 2:
    mi_eleccion = asignacion(eleccion_jugador)
  else:
    print('Lo siento, no introduciste un valor valido. Intenta de nuevo')

  eleccion_enemiga = asignacion_enemiga()
  print('Y tu oponente eligió ', eleccion_enemiga)
  
  if mi_eleccion == eleccion_enemiga:
    print('Vaya. Parece que es uin empate, vamos a intentarlo de nuevo!')
  elif (mi_eleccion == 'Piedra 🪨' and eleccion_enemiga == 'Tijeras ✂️') or (mi_eleccion == 'Tijeras ✂️' and eleccion_enemiga == 'Papel 📃') or (mi_eleccion == 'Papel 📃' and eleccion_enemiga == 'Piedra 🪨'):
    vidas_enemigo -= 1
    print(f'Excelente! Vamos a Festejar!! Ganaste! 🥳🎊🎉 \n Marcador: \n Vidas del Jugador :{vidas_jugador} \n Vidas del oponente:{vidas_enemigo}')
    print('✅'*20)
  else:
    vidas_jugador -= 1
    print(f'Rayos. Parece que ganó la Maquina. 🤕 Vamos a volver a intentarlo. \n Marcador: \n Vidas del Jugador :{vidas_jugador}  \n Vidas del oponente:{vidas_enemigo}')
    print('💀'*30)

  if vidas_jugador == 0:
    print("Parece que perdiste! 💀👻 Mas suerte a la proxima")
    break
  elif vidas_enemigo == 0:
    print("Ganaste! 🕺💃 Vamos a festejar")
    break