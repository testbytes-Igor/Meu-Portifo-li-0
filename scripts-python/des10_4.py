dis= float(input('Digite a distancia da viagem:'))
print('Voce esta prestes a realizar uma viagem de {}km.'.format(dis))
if dis <= 200:
    p= dis * 0.50
    print('A distancia da viagem é {} e o valor a pagar ficou R${}'.format(dis,p))
else:
    p2= dis * 0.45
    print('A distancia de sua viagem é {} e o valor PROMOCIONAL ficou R${}'.format(dis, p2))