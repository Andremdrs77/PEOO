import pandas

numeros = pandas.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

numeros.to_excel('numeros.xlsx')