
# 1°Desafio Listas (criando listas)
'''
Neste desafio gostaria que você criasse uma lista chamada 'frutas'
que comtenha os seguintes itens: "maçã", "banana", "manga" e "uva"
depois disso quero que você imprima esta lista na tela.
'''
print('1°Desafio\n')

frutas = ['maçã', 'banana', 'manga', 'uva']
print(frutas)
print("\n========================\n")


# 2°Desafio Listas (Manipulando lista)

'''
Para este desafio quero que você use a lista frutas do desafio
anterior Seu desafio é imprimir o primeiro e o ultimo iten da lista.
'''
print('2°Desafio\n')


print(f'O primeiro iten é :{frutas[0]}')
print(f'\nO ultimo iten é :{frutas[-1]}')
print("\n========================\n")


# 3° Desafio Listas (index lista)

'''
Seu desafio é alterar o segundo elemento da lista para 'morango'
depois disto adicione a fruta 'abacaxi' ao final da lista.
Por fim imprima a lista na tela.
'''
print('3°Desafio\n')


frutas[1] = 'morango'
frutas.append('abacaxi')
print(frutas)
print("\n========================\n")


# 4° Desafio Listas (remover iten da lista)

'''
Primeiro remova o iten manga da lista 
depois disto remova o ultimo iten da lista.
Por fim imprima a lista na tela
'''
print('4°Desafio\n')


frutas.remove('manga')
print(frutas)
print()
frutas.__delitem__(-1)
print(frutas)
print("\n========================\n")


# 5° Desafio Listas (lista com loops)

'''
Use um "for loop" para percorrer a lista e imprima cada fruta
precedida pelo texto "Eu gosto de".
'''
print('5°Desafio\n')


for fruta in frutas:
    print(f'Eu gosto de: {fruta}')
