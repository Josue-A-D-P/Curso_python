# Desafio calculo fatorial

'''
Crie uma função que calcule o fatorial de um numero e imprima o resultado na tela .
'''

def fatorial(num):
    contador = 0
    pare = num - 1
    while num > 1 :
        contador += 1
        print(contador)
        num = num - 1
        num = num * num
        print (num)    
        if contador == pare:
            break




user_num = int(input("digite um numero: "))

fatorial(user_num)