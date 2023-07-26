# Desafio com if,elif,else

'''Criar um programa que dependendo da temperatura (em celsius) do steak
   ele retorna o ponto de cozimento em português. O usuário deverá
   fornecer a temperatura. 
   
   
   Temperatura - cozimento
   
   48° = Selada
   54° = Ao ponto para mal
   60° = Ao ponto
   65° = Ao ponto para bem
   71° = Bem passada
   '''

temperatura = int(input ('Qual é a temperatura da carne? '))

if temperatura < 48:
    print('cozinhar por mais alguns minutos')

elif temperatura >= 48 and temperatura < 54:
    print('Selada')

elif temperatura >= 54 and temperatura < 60:
    print('Ao ponto para mal')

elif temperatura >= 60 and temperatura < 65:
    print('Ao ponto')

elif temperatura >= 65 and temperatura < 71:
    print('Ao ponto para bem')

elif temperatura >= 71 and temperatura <= 75:
    print('Bem passada')

else:
    temperatura > 75
    print('A carne está queimada')
