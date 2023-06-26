#Unpacking list
#Extrair variaveis(dados) de uma lista

produtos = ['arroz', 'feijão', 'laranja', 'banana']

#forma convencional
'''
iten1 = produtos[0]
iten2 = produtos[1]
iten3 = produtos[2]
iten4 = produtos[3]

print(iten1)
print(iten2)
print(iten3)
print(iten4)'''

#forma simplificada:
iten1, iten2, iten3,*outros = produtos

print(iten1)
print(iten2)
print(iten3)
print(outros)