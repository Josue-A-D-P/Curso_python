# Set (listas)
# Similar a listas 
# Evita itens duplicados
# Não utiliza index

lista_1 = set([1, 2, 3, 5, 6])

print(lista_1)
print()

s1 = {1, 2, 3, 4, 5, 6}
print(s1)

s1.add(7) # adiciona um iten 
print(s1)

s1.update([8,9,10]) # adiciona varios itens
print(s1)

s1.remove(1) # remove iten mas se ele não existir retorna erro
print(s1)

s1.discard(90) # remove iten e se ele não existir não retorna erro
print(s1)