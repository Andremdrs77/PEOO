
# while True:
#     try:
#         escrever = input('O que escrever no arquivo? ("pare" para parar): ')
#         arquivo = open('nomes.txt', 'a')

#         if escrever.upper() == 'PARE':
#             arquivo.close()
            
#         arquivo.write(eskrever)

#     except Exception as erro:
#         print("Erro: ", erro)
#         print("Classe do erro: ", type(erro))

#     finally:
#         break

try: 

    from arquivo1 import coisaquenãoexiste

except ImportError as erro:

    print('Erro:', {erro})

    print('Classe do erro:', {type(erro)})