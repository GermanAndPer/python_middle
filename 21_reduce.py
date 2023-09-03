import functools

numbers = [2, 3, 4, 5]

reduce_var = functools.reduce(lambda contador, elemento: contador + elemento, numbers)

suma = sum(numbers)

print(reduce_var)
print(suma)

names = ['German', 'Rodrigo', 'Aaron', 'Samu']

reduce_names = functools.reduce(lambda contador, elemento: contador + elemento, names)
print(reduce_names)