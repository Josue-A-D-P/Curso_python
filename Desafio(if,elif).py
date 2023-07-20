import math

# Calculo de IMC "indice de massa corporal"

'''
Qual é a sua altura em cm:
Qual é o seu peso em kg:
'''

# Menor que 18,5 = Magreza
# Entre 18,5 e 24,9 = Normal
# Entre 25 e 29,9 = Sobrepeso
# Entre 30 e 39,9 = Obesidade
# Maior que 40 = Obesidade grave


altura =float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg:: '))

imc = peso / (altura / 100) ** 2 

if imc < 18.5:
    print(f'Magreza')

elif imc >= 18.5 and imc <= 24.9:
    print('Normal')

elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso') 

elif imc >= 30 and imc <= 39.9:
    print('Obesidade')

else:
    imc >= 40
    print('Obesidade grave')