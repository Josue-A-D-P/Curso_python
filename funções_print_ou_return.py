# return retornão um valor para o sistema
# print realizam uma tarefa

def calcule1(valor1,valor2):
    result = valor1 + valor2
    print(result)


def calcule2(valor1,valor2):
    result = valor1 + valor2
    return result


calcule1(100,100)
calcule2(50,50)


x = calcule1(100,100)
y = calcule2(50,50)


#A variavel x retorna none por que não recebeu nenhum valor com o comando print por ser uma tarefa 
#A variavel y retorna o resultado por que recebeu o valor com o comando return que armasena o valor


print(x)
print(y)