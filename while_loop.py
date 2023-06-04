# while loop
'''Exelente para loops dependentes de uma condição'''
#Crie uma promoção decrecente com o stop em R$25 para um produto que vale R$100.

valor = 100
dia = int (input('Digite o dia em que a promoção inicia: '))
while valor > 20:
    dia += 1
    print(f'No dia {dia} o produto vai ser vendido por:R$ {valor}.00')
    valor -= 5