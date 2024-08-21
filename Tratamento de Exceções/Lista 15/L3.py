senha = input("Crie uma senha: ")

if len(senha) < 8:
    raise Exception('A senha deve ter ao menos 8 caractéres!')

elif senha.upper() == 'INTERNACIONAL':
    raise Exception('Essa senha não é Roberto Carlos suficiente!')

else:
    print("Senha criada com sucesso!")