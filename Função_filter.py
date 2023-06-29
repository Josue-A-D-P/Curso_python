#Filter function
    #Muito utilizado com listas
    #Aplicar uma função a um interable, filtrando os itens(list, tuple, dict etc.)


valores = [10, 12, 34, 44, 57]

'''def remove20(x):
    return x > 20


print(list(filter(remove20, valores)))'''


print(list(filter(lambda x: x > 20, valores)))