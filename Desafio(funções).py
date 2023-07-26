# Desafio com funções

'''
Criar um programa que calcule a quantidade de tinta nessecária para
pintar uma parede . O usuário deverá fornecer as seguintes informações:
Rendimento, Altura e Largura.
O programa devera mostrar na tela a mensagem ' Voce necessita de x 
latas de tinta'.
'''

rendimento = float (input('Qual é o rendimento da lata de tinta? '))
print()
altura = float (input('Qual é a altura da parede? '))
print()
largura = float (input('Qual é a largura da parede? '))
print()

def quant_tinta() :
    area = altura * largura / rendimento
    print(f'Você necessita de {area} latas de tinta')

quant_tinta()