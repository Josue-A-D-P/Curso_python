# Desafio Par e impar

'''
Para este desafio crie uma lista de numeros de 1 a 10. Use um for loop
para iterar sobre a lista.Se o numero atual da iteração for par imprima 
"O numero [numero] é par",Se o numero for impar imprima "O numero [numero] é impar".
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(f"O numero {numero} é par")
    else:
        print(f"O numero {numero} é impar")