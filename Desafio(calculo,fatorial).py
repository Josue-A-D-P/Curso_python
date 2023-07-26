# Desafio calculo fatorial

'''
Crie uma função que calcule o fatorial de um numero e imprima o resultado na tela .
'''

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

user_num = int(input('Digite um numero: '))
print(f'O fatorial de {user_num} é {fatorial(user_num)}')