vel= float(input('Qual a velocidade do veículo? '))
if vel > 80:
    print('Voce ultrapassou o limite de 80km/h e foi multado!')
    m= (vel-80) * 7
    print('Voce deve pagar uma multa de R${:.2f} pela infração!'.format(m))
print('Tenha um otimo dia! Dirija com atenção!')
