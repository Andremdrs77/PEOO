try:
    import matematica as math
    Resultado = math.cos(30)
except ModuleNotFoundError:
    print('Esta biblioteca não existe!')
    
try:
    Resultado = math.cos(30)
except NameError:
    print("math.cos(30) não pode ser executado, pois 'math' não existe.")