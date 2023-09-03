def run():
  word = input('¿Que palabra o Frase quieres validar? ')
  variations = {
    'Original': word
  }
  variations['Mayusculas'] = word.upper()
  variations['Minusculas'] = word.lower()
  variations['Nom Prop'] = word.title()
  print(variations)
  return variations


if __name__ == '__main__':
  run()

print(__name__)