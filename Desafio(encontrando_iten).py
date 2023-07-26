# Desafio encontrando iten com while loop

'''
Para este desafio crie um loop que peça ao usuário para digitar 
o nome de uma fruta,Se a fruta digitada não for "abacate",o loop
deve continuar pedindo ao usuario para digitar o nome de uma fruta,
Se a fruta for "abacate",o loop deve terminar e o programa deve imprimir
"Parabéns vecê acertou a fruta!.
'''

fruta = ""

while fruta.lower() != "abacate":
    fruta = input('Digite o nome de uma fruta: ')
print("Parabéns vecê acertou a fruta!")
