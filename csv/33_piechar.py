import csv
import matplotlib.pyplot as plt

def read_csv(path):
  with open(path,'r') as csvfile:
    lectura = csv.reader(csvfile,delimiter=',')
    header = next(lectura)
    data = []
    for row in lectura:
      iterable = zip(header, row)
      country_dictionary = {key: float(value) for key, value in zip(header, row) if key == 'World Population Percentage'}
      data.append(country_dictionary)
    return data


def ordered_lists(data):
  just_year = []
  just_population = []
  for element in data:
    for item in element:
      just_year.append(item)
      print('ITEM => ',item)
      just_population.append(element[item])
      print('ELEMENT => ',element[item])
  #print('Años => ',just_year)
  #print('Poblaciones => ',just_population)
  #print(just_year)
  #print(just_population)
  return just_year, just_population

#def my_fist_barchart(labels, values):
def my_fist_piechart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  data = read_csv('./csv/data.csv')
  #labels, values = data
  print(data)
  labels, values = ordered_lists(data)
  barras = my_fist_piechart(labels, values)
