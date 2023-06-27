#set (listas)
#Similar a listas 
#Evita itens duplicados
#Não utiliza index

lista_1 = [10, 20, 30, 40, 50]
lista_2 = [10, 20, 60, 70]

num_1 = set(lista_1)
num_2 = set(lista_2)

print(num_1)
print(num_2)

print()

print(num_1 | num_2) # Union
print(num_1 - num_2) # Difference
print(num_1 ^ num_2) # Symmetric Difference
print(num_1 & num_2) # And