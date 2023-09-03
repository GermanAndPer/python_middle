import csv
import matplotlib.pyplot as plt

def read_csv(path):
  with open(path,'r') as csvfile:
    lectura = csv.reader(csvfile,delimiter=',')
    header = next(lectura)
    data = []
    
    for row in lectura: 
      iterable = zip(header, row)
      country_dictionary = {key: value for key, value in zip(header, row)}
      data.append(country_dictionary)
    return data


def ordered_lists(data):
  labels = []
  values = []
  continente = input('Que continente revisamos? ')
  for element in data:
    if element['Continent'] == continente:
      for item in element:
      
        if item == 'Country/Territory':
          labels.append(element[item])
          #print('ITEM => ',element[item])
        if item == 'World Population Percentage':
          values.append(float(element[item]))
          #print('VALUES => ',element[item])

  
  #print('Años => ',just_year)
  #print('Poblaciones => ',just_population)
  #print(just_year)
  #print(just_population)
  return labels, values

def my_fist_piechart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  data = read_csv('./csv/data.csv')
  #labels, values = data
  print(data[0])
  labels, values = ordered_lists(data)
  barras = my_fist_piechart(labels, values)
