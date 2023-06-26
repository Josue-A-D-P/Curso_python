#Verificando itens dentro de uma lista:

cores = ['Amarelo', 'Verde', 'Azul', 'Branco', 'Preto', 'Vermelho']


consulta_cor = input('Digite a cor: ')

#O método .title está sendo utilisado para garantir que o programa vai receber a entrada desejada.
if consulta_cor.title() in cores:
    print('Disponivel em estoque.')
else:
    print('Indisponivel em estoque.')