import os

class ContaCorrente():
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        
    def verSaldo(self):
        os.system('cls')
        print(f'Cliente: {self.nome} | Saldo da Conta Corrente: R${self.saldo:.2f}')

    def depositar(self, valor):
        os.system('cls')
        self.saldo += valor
        print('Depositado com sucesso!')

    def sacar(self, valor):
        os.system('cls')
        try:
            if valor > self.saldo:
                raise ValueError('O valor inserido é maior que o do saldo!')
        except Exception as erro:
            print(f'Erro: {erro}')
            print(f'Classe do erro: {type(erro)}')
        else:
            self.saldo -= valor

    def sair(self):
        os.system('cls')
        print("Saindo...")
        exit()


usuario = ContaCorrente('Vasco')

while True:
    print('''
    =======================================
    Banco Internacional
    =======================================
    [1] Consultar Saldo
    [2] Depositar
    [3] Sacar
    [0] Sair
    ''')
    opcao = int(input('Informe a Opção: '))

    if opcao == 1:
        usuario.verSaldo()
    
    elif opcao == 2:
        deposito = float(input(f"Valor a depositar para {usuario.nome}: "))
        usuario.depositar(deposito)

    elif opcao == 3:
        saque = float(input(f"Valor do saque para {usuario.nome}: "))
        usuario.sacar(saque)

    elif opcao == 0:
        usuario.sair()