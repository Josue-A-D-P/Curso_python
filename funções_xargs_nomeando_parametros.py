#Varios argumentos identificando os parametros
#Criar uma função que armazena numeros e strings (dados)

def agencia(**carro):
    return carro


x = agencia( Veiculo = 'Gol', Cor = 'Branco', Placa = 12345 )
y = agencia( Veiculo = 'Palio', Cor = 'Preto', Placa = 13557, Ano = 2011 )
print(x)
print(y)