from random import randint
computador = randint(0,5) #Faz o computador pensar no numero
#print('Pensei no numero...{}'.format(computador))
print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar..')
print('-=-' *20)
jogador = int(input('Em que numero eu pensei..?'))
if jogador == computador:
    print('Voce GANHOU!')
else:
    print('É.. eu VENCI! Escolhi o numero {}, não o {}.'.format(computador, jogador))
