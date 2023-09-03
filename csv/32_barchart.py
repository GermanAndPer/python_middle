import csv
import matplotlib.pyplot as plt

def read_csv(path):
  with open(path,'r') as csvfile:
    lectura = csv.reader(csvfile,delimiter=',')
    header = next(lectura)
    data = []
    for row in lectura:
      iterable = zip(header, row)
      country_dictionary = {key.replace(' Population',''): int(value) for key , value in zip(header, row) if key.endswith('lation')}
      data.append(country_dictionary)
    return data


def ordered_lists(data):
  just_year = []
  just_population = []
  for element in data:

    for item in element:
      just_year.append(item)
      #print('ITEM => ',item)
      just_population.append(element[item])
      #print('ELEMENT => ',element[item])
  #print('Años => ',just_year)
  #print('Poblaciones => ',just_population)
  #print(just_year)
  #print(just_population)
  return just_year, just_population


def my_fist_barchart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

if __name__ == '__main__':
  data = read_csv('./csv/data.csv')
  #labels, values = data
  #print(data[0])
  labels, values = ordered_lists(data)
  
  barras = my_fist_barchart(labels, values)

'''
{
  'Rank': '36', 
  'CCA3': 'AFG', 
  'Country/Territory': 
  'Afghanistan', 'Capital': 
  'Kabul', 'Continent': 'Asia', 
  '2022 Population': '41128771', 
  '2020 Population': '38972230', 
  '2015 Population': '33753499', 
  '2010 Population': '28189672', 
  '2000 Population': '19542982', 
  '1990 Population': '10694796', 
  '1980 Population': '12486631', 
  '1970 Population': '10752971', 
  'Area (km²)': '652230', 
  'Density (per km²)': '63.0587', 
  'Growth Rate': '1.0257', 
  'World Population Percentage': '0.52'
  }

{
  '2022': 41128771, 
  '2020': 38972230, 
  '2015': 33753499, 
  '2010': 28189672, 
  '2000': 19542982, 
  '1990': 10694796, 
  '1980': 12486631, 
  '1970': 10752971
  }
  '''