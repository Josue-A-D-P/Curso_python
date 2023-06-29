# List comprehension:
    # Mais simples de se escrever
    # Utilizado quando voce precisa criar uma nova lista a partir de uma existente
    # expreção for item in items

frutas1 = ['abacate', 'banana', 'morango', 'kiwwi', 'abacaxi']
'''frutas2 = []

for itens in frutas1:
    if 'b' in itens:
        frutas2.append(itens)
        
print(frutas2)'''


frutas2 = [iten for iten in frutas1 if 'b' in iten]

print(frutas2)

