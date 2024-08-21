import warnings
contatos = []
get = []

while True:
    try:
        nome = input('Nome ("Fim" para sair): ')
        if nome.upper() == 'FIM':
            print("Saindo...")
            break

        elif 'X' in nome.upper():
            raise UserWarning('Nome não pode conter a letra "X"!')
        
    except UserWarning as erro:
        print(f"Erro: {erro}")
        print(f"Classe do erro: {type(erro)}")


    else:
        try:
            telefone = input('Telefone ("Fim" para sair): ')
            if telefone.upper() == 'FIM':
                print("Saindo...")
                break

            elif telefone.isnumeric() == False:
                raise UserWarning('Telefone só pode conter valores numéricos')

        except UserWarning as erro:
            print(f"Erro: {erro}")
            print(f"Classe do erro: {type(erro)}")

        else:
            get.append(nome)
            get.append(telefone)
            contatos.append(get[:])
            get.clear()

for cont, pessoa in enumerate(contatos):
    print(contatos[cont])