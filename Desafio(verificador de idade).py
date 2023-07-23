# Desafio verificador de idade 

'''
Para este desafio peça ao usuario para digitar sua idade se a idade for
menos de 13 imprima "Você é uma criança", Se a idade estiver entre 13 e 19
imprima "Você é um adolecente", Se a idade for 20 ou mais imprima 
"Você é um adulto".
'''

idade = int(input('Digite sua idade: '))


if idade < 13:
    print("Você é uma criança")

elif idade >= 13 and idade < 20:
    print("Você é um adolecente")

else:
    print("Você é um adulto")