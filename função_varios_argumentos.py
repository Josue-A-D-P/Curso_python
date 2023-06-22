#Função com varios argumentos
#Criar uma função que soma varios numeros

def soma(*numeros):
    result = 0
    for num in numeros:
        result += num
    return result


x = soma(2,4,6,7)

print(x)