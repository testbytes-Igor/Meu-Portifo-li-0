print('-=-'*20)
print('-----Analisador de triangulos--------')
print('-=-'*20)
r1= float(input('Digite o primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3= float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triangulo com essas medidas.')
else:
    print('Não conseguimos formar um triangulo com essas medidas, tente novamente.')
