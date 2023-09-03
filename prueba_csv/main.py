import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path,'r') as csvfile:
      lectura = csv.reader(csvfile,delimiter=',')
      numbers = []
      for row in lectura:
        numbers.append(int(row[1]))
      total = sum(numbers)   
      #print(numbers)
   
   return total

response = read_csv('./prueba_csv/data.csv')
print(response)