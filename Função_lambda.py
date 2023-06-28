# Lambda function
# È uma função pequena (sem nome)
# Pode ter varios argumentos mas só uma expreção
# Muito utilizada dentro de outras funções
# Código mais 'clean'


# Função convencional
def somar(x):
    return x + 10


print(somar(2))    
print()

# Lambda mesmo resultado uma linha linha de codigo
calcular = lambda x: x + 10

print(calcular(2))