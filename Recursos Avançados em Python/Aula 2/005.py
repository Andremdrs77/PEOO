import pandas

amigos = pandas.read_csv('amigos.csv')
amigos.to_json('amigos.json')