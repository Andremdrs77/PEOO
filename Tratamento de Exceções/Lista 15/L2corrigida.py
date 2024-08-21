#Questão corrigida em sala
try:
    arquivo = open('nomess.txt', 'r')
    contador = 1
    for linha in arquivo:
        print(f'Linha[{contador}] -> {linha}', end='')
        contador += 1
    arquivo.close()

except FileNotFoundError as erro:
    print(f'Erro: {erro}')
    print(f'Classe do erro: {type(erro)}')