# Map function
    # Muito utilizada com listas
    # Aplicar uma função a um iterable, por item (lista, tuple ,dic...)

lista1 = [1, 2, 3, 4]

def mult(x):
    return x * 2

lista2 = map(mult,lista1)
print(lista2)
print()
print(list(lista2))