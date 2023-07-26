# 1° Desafio for loop (contando com for loop)

'''
Para este desafio quero que você use a função range()
em um "for loop" para imprimir os numeros de 1 a 10 na tela.
'''
print('1° Desafio')

for x in range(1, 11):
    print(x)
print('\n=======================\n')


# 2° Desafio for loop (Nested for loop)

'''
Para este desafio crie uma lista de frutas e outra de vegetais.
Use um (Nested for loop) para imprimir todas as combinações possiveis 
de frutas e vegetais , com a fruta primeiro e o vegetal em segundo
'''

frutas = ['morango', 'banana', 'abacaxi']
vegetais = ['alface', 'couve', 'brócolis']

for fruta in frutas:
    print()
    for vegetal in vegetais:
        print(fruta,vegetal)