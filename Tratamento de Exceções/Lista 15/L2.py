while True:
    nomes = []
    try:
        escrever = input('O que escrever no arquivo? ("pare" para parar e "ler" para ler): ')
        arquivo = open('nomes.txt', 'a')

        if escrever.upper() == 'PARE':
            arquivo.close()
            break

        arquivo.write(escrever + '\n')

        if escrever.upper() == 'LER':
            for registro in arquivo.readlines():
                print(registro)

    except Exception as erro:
        print("Erro: ", erro)
        print("Classe do erro: ", type(erro))
        arquivo.close()
