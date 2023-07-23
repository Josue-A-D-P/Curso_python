# Desafio procurar em lista

'''
Para este desafio você tem uma loja de carros, crie uma lista com os carros 
que você tem em estoque: BMW X6, BMW I5, BMW I8. Peça ao usuario para que ele 
insira o nome do carro que deseja comprar, Se o carro estiver em estoque,
imprima "Este carro está disponivel", Se o carro não estiver em estoque 
imprima "Desculpe este carro não está disponivel".
'''

estoque = ['BMW X6', 'BMW I5', 'BMW I8']

pesquisa_carros = input('Digite o nome do carro: ')

if pesquisa_carros in estoque:
    print("Este carro está disponivel")
else:
    print("Desculpe este carro não está disponivel")