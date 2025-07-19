#if carro.esquerda():
   # bloco True
#else:              #Nunca será executado as duas condições
   # bloco False
tempo= int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('----FIM-----')
#----------------------------------
tempo2= int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <=3 else 'Carro Velho')
print('------FIM------')

