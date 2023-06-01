'''' Operações matematicas'''
#Primeiro parenteses 
#Segundo exponenciais
#Terceiro multiplicação e divisão
#Por ultimo adição e subtração

calculo = 2 + 2 * 3 / 2
calculo2 = (2 + 2) * 3 / 2
calculo3 = (2 + 2) * 3 / 2 ** 3

print(calculo)
print(f'\n{calculo2}')
print(f'\n{calculo3}')

''' Operadores de comparação'''
 # == Equal
 # != Not Equal
 # > Greater then
 # < Less then
 # >= Greater then or equal to
 # <= Less then or equal to

operador = 'banana' == 'Banana'
print (f"\n{operador}")

operador = 'banana' != 'Banana'
print (f"\n{operador}")

operador = 10 > 13
print(f"\n{operador}")

operador = 10 < 13
print(f"\n{operador}")

operador = 10 >= 13
print(f"\n{operador}")

operador = 10 <= 13
print(f"\n{operador}")

''' assignment operators (Operadores de atribuição) '''

x = 10
x = x + 5
print(x)

x = 10
x += 5
print(x)

x = 10
x -= 5
print(x)

x = 10
x *= 5
print(x)

x = 10
x /= 5
print(x)

x = 10
x %= 3
print(x)