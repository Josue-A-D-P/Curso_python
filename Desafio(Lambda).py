# 1° Desafio Lambda

'''
Para este desafio crie uma função lambda que aceite um numero e retorne 
o cubo desse numero. 
'''
print('1° Desafio\n')

num = int(input('Digite um numero: '))

cubo = lambda num: num ** 3
print(f'O cubo de {num} é : {cubo(num)}')
print('\n=========================\n')


# 2° Desafio Lambda

'''
Para este desafio crie uma função lambda que aceite dois numeros e 
retorne a multiplicação desses dois numeros.
'''

print('2° Desafio\n')

mult = lambda valor1,valor2: valor1 * valor2


valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite segundo valor: '))

print(f'O resultado de {valor1} multiplicado por {valor2} é : {mult(valor1,valor2)}')
print('\n=========================\n')


# 3° Desafio Lambda com if else

'''
Para este desafio crie uma função lambda que aceite um numero e retorne
"par" se for par e "impar" se for impar.
'''

print('3° Desafio\n')

impar_par = lambda num : 'par' if num % 2 == 0 else 'impar'

num = int(input('Digite um numero: '))

print(f'O numero {num} é {impar_par(num)}')