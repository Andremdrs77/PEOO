try:
    exec("while True print('Hello World!')")
except Exception as erro:
    print('Erro:', erro)
    print('Classe do erro:', type(erro))

#Usei um método que o senhor não ensinou, porém usei apenas para não deixar a questão em branco,
#pois não sabia uma forma de tratar erro de síntaxe

#outra forma seria...

# try:
#     while True:
#         print("Hello World!")
#         raise Exception('Não faça prints infinitos, rapaz!')
# except Exception as erro:
#     print(f'Erro: {erro}')
#     print(f'Classe do Erro: {type(erro)}')

#...Porém eu apenas previno um erro que eu mesmo inventei (prints infinitos inúteis), após ter CORRIGIDO a síntaxe,
#por isso não dei a solução como correta. 