while True:
    num = input("Insira um número para calcular uma raíz REAL ou digite 'Sair': ")

    if num.upper() == 'SAIR':
        break
    
    num = int(num)

    if num < 0:
        raise ValueError('Não existe raíz negativa nos números reais!')
    else:
        raiz = num ** (1/2)
        print(f"A raíz de {num} é {raiz}")