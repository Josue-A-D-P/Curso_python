'''
Neste desafio,quero que você crie um script
que solicite ao usuario dois numeros.
Em seguida seu script deve imprimir a soma,
a subtração,a multiplicação,a divisão (resultado decimal),
e a exponenciação (primeiro número elevado ao segundo número) desses dois números.
'''


num1 = float (input('Digite o primeiro valor: '))
num2 = float (input('Digite o segundo valor: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2

print(f'A soma é :{soma}')
print(f'A subtração é :{subtracao}')
print(f'A divisão é :{divisao}')
print(f'A multiplicação é :{multiplicacao}')
print(f'A exponenciação é :{exponenciacao}')
