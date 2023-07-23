# Desadio cntador de listas com for loop

'''
Para este desafio crie uma lista de frutas que inclui 'maçã' 3 vezes
e outras frutas de sua escolha use um loop for para contar quantas
vezes "maçã" aparece na lista imprima o resultado.
'''

frutas = ['maçã', 'banana', 'maçã', 'uva', 'morango', 'maçã']
total = 0


for fruta in frutas:
    if fruta == 'maçã':
        total += 1
print(f'Maçã aparece {total} vezes na lista')