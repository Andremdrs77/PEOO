import pandas

numeros = pandas.Series([10, 20, 30, 40])

numeros2 = pandas.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print(numeros)
print('=============')
print(numeros2)
print('====')
print(numeros2['c'])

#print(type(numeros))