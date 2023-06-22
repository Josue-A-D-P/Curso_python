#Listas:
''' Adicionar mais de uma informação em variaveis
    Manter a sequencia dos dados em uma variavel  '''
#Funções em listas

paises = ['Brasil', 'Portugal', 'Canadá', 'Africa']

#.append() Adiciona um itens ao fim da lista
paises.append('Alemanha')
print(paises)


#.remove() Remove o itens da lista
paises.remove('Brasil')
print(paises)


#.insert() adiciona itens na posição estipulada
paises.insert(0,'Brasil')
print(paises)


#.pop() retirar itens estipulados pelo index da lista
paises.pop(1)
print(paises)


#.sort() Organisa em orden alfabetica
paises.sort()
print(paises)