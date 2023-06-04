
#Separando as letras da palavra com for loop

palavra = input('Digite uma palavra: ')

for espaco in palavra:
    print(f'{espaco}', end= ' ')

print('\n---------------\n')


#for loop criando retangulo
linhas = 4
colunas = 15
simbolo = '@'
for l in range(linhas):
    for c in range(colunas):
        print(simbolo,end= "")
    print()