# Erros
    # Exelenete para testes
    # Nao realiza o 'stop' no programa
    # Mensagens customizadas quando encomtra um erro


try:
    valor = int(input('Digite o valor do produto: '))
    print(valor)
except ValueError:
    print('Favor digite um valor valido')
#finally:
    #print('Processando...')
else:
    resultado = valor * 2
    print(resultado)

print()
print('codigo continua após o erro')