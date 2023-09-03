#FILTER
#Es un filtro de Python
#Se usa igual que MAP pero con la palabra reservada FILTER

numeros = [1,2,3,4,5]
#para este caso, tal cual no ponemos el valor que devolver.
#Mas bien hace una comprobacion
#Y si la comprobacion es verdadera, guarda el valor evaluado. 
numeros_pares = list(filter(lambda numbero : numbero % 2 == 0, numeros))
print(numeros_pares)





matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)

#FILTER DICTIONARY
#Hacemos exactamente la misma validacion.
#Solo al momento de hacer la validacion, no olvidar el nombre de la CLAVE
filtros = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(filtros)
print(matches)