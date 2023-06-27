#set (listas)
#Similar a listas 
#Evita itens duplicados
#Não utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
print(set4)

set5 = set1.difference(set3)
print(set5)

set6 = set1.intersection(set2)
print(set6)

set7 = set1.symmetric_difference(set3)
print(set7)