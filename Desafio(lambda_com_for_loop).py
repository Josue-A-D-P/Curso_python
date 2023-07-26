# Desafio Lambda com for loop

'''
Para este desafio crie uma função lambda que eleve um numero ao quadrado 
em seguida use esta função para calcular o quadrado de todos os numeros 
de uma lista usando um for loop
'''

quadrado = lambda num: num ** 2

lista = [1, 2, 3, 4, 5, 6]
resultado = []

for i in lista:
    resultado.append(quadrado(i))

print(f'O resultado dos numeros {lista} é:\n{ resultado}')