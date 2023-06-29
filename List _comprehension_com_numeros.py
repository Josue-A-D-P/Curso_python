# List comprehension:
    # Mais simples de se escrever
    # Utilizado quando voce precisa criar uma nova lista a partir de uma existente
    # expreção for item in items

'''valores = []

for x in range(6):
    valores.append(x * 10)

print(valores)'''

valores = [x * 10 for x in range(6)]
print(valores)