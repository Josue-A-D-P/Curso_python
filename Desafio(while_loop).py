# 1° Desafio While loop (contador 1 a 10)

'''
Para este desafio quero que você use while loop 
para imprimir os numeros de 1 a 10 na tela
'''

print('1° Desafio')
num = 0
while num < 10:
    num += 1
    print(num)
print('\n=======================\n')

# 2° Desafio While loop (while loop com breack e continue)

'''
Para este desafio crie um loopque imprima os numeros de 1 a10 
mas que pare de imprimir assim que chegar a 5 usando o comando 
"breack". Em seguida crie um segundo loop que imprima os numeros de 1 a 10
mas pule a imprenção do numero 5 usando o comando "continue".
'''

print('2° Desafio')
num = 0
while num < 10 :
    if num == 5:
        break
    num += 1
    print(num)

print('\n2° Desafio')
num = 0
while num < 10 :
    num += 1
    if num == 5:
        continue
    print(num)