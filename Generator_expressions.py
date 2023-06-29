from sys import getsizeof

# Generator expressions
    # Uma forma mais rapida para listas, dicionarios e etc.
    # Menos memória alocada
    # Valores em bytes

numeros = [x * 10 for x in range(100)]

print(type(numeros))
print(numeros)
print(getsizeof(numeros))


print('==============')


numeros = (x * 10 for x in range(100))

print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))