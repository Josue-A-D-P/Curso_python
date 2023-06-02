'''enviar email com detalhes da compra online
com (maximo de 3 tentativas) para compras confirmadas'''

compra_confirmada = True
dados_da_compra = 'Compra no valor de 12.50 e entrega confirmada!'
for enviar in range(3):
    if compra_confirmada:
        print(dados_da_compra)
        print('Enviamos os detalhes da compra para seu email!')
        break
else:
    print('Falha na compra!')