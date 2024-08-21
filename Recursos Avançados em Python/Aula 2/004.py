import pandas

agenda = {'nome':['Maria', 'Pedro','Chico',], 'Telefone': ['2222-2222', '3333-3333', '4444-4444']}
planilha = pandas.DataFrame(agenda)
#print(planilha)
#print(planilha.count())
print(planilha.iloc[1][1])

planilha.to_excel('planilha.xlsx')

planilha.to_csv('amigos.csv', header=None)