print("Olá\n")
nome = input ('Qual seu nome? ')
idade = input ('Qual sua idade? ')
idade = str(idade)
print('O ' + nome + ' tem ' + idade + ' anos ' + 'de idade ')

'''Manipulando dados da variavel
calculando idade'''

ano_nacimento = input ('\nEm que ano voce naceu? ')
ano_atual = int(2023)
idade = ano_atual - int(ano_nacimento)
print(idade)
