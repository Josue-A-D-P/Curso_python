# Desafio Duas funções

'''
Para este desafio crie duas funções a primeira função deve aceitar um numero
e retornar o dobro desse numero. A segunda função deve aceitar um numero e retornar 
o quadrado desse numero. em seguida chame a primeira função dentro da segunda para 
retornar o quadrado do dobro desse numero.
'''

def dobro(num):
    return num * 2


def quadrado(num):
    return dobro(num) ** 2


user_number = int(input("Digite um numero: "))

print(f'O quadrado do dobro de {user_number} é: {quadrado(user_number)}')