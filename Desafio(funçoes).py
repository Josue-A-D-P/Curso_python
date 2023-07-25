# 1° Desafio função simples

'''
Crie uma função que aceita um número como entrada e retorna o quadrado deste número.
'''

def quadrado(numero):
    return numero ** 2


print('1° Desafio\n')
num = int(input('Digite um numero: '))

print(f'\nO quadrado de {num} é {quadrado(num)}')
print('\n====================\n')


# 2° Desafio Soma com funções

'''
Para este desafio crie uma função que aceite dois numeros como entrada
e retorne a soma desses numeros.
'''

def soma(valor1,valor2):
    return valor1 + valor2


print('2° Desafio\n')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))


print(f'O resultado da soma entre {valor1} e o numero {valor2} é:  {soma(valor1,valor2)}')
print('\n====================\n')


# 3° Desafio calculando base e expoente

'''
Para este desafio, crie uma função que calcule a potência de um numero
A função deve aceitar dois argumentos: a base eo expoente,no entanto 
se o expoente não for fornecido ao chamar a função,ele deve assumir
o valor padrão de 2.
'''


def potencia(base,expoente=2) :
        return base ** expoente

print('3° Desafio\n')

user_base = int(input('Digite a base: '))
user_expoente = input('Digite o expoente: ')

if user_expoente:
    print(f'O resultado é: {potencia(user_base,int(user_expoente))}')
else:
    print(f'O resultado é: {potencia(user_base,)}')
