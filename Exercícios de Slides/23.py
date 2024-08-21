import json, requests

dominio = input('Insira uma sigla: ')

consulta = requests.get(f'https://brasilapi.com.br/api/registrobr/v1/{dominio}')

print(consulta.status_code)

if consulta.json()['status'] == 'AVAILABLE':
    print("Domínio disponível!")
else:
    print("Domínio não disponível.")