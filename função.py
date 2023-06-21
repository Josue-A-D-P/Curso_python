# Functions (Funções)

# DRY - Don't repeat yourself

def somar_dois_numeros():
    numero1 = int (input ('Digite o primeiro numero: '))
    numero2  = int (input ('Digite o segundo numero: '))
    resultado =  numero1 + numero2
    print(f'O resultado é {resultado} .')


somar_dois_numeros()