frase= "Curso em Video Python"
print(frase)
print('-----------------------------------')
frase2= 'Curso em Video Python'
print(frase2[3])
print('-----------------------------------')
frase3= 'Curso em Video Python'
print(frase3[3:13])
print('-----------------------------------')
frase4= 'Curso em Video Python'
print(frase4[3::3])
frase5= 'Curso em Video Python'
print(frase5[:5])
print('------------------------------------')
frase6= 'Curso em Video Python'
print(frase6[:20:2])
print('-------------------------------------')
frase7= 'Curso em Video Python'
print(frase7[::2])
print('=======================================')

print("""Hoje vamos pensar mais sobre isso, ok?
      vamos ver o que podemos fazer por voce
      acho que consigo te ajudar
      mas eu não quero sua ajuda, ok?""") #Para escrever frases longas em um unico print utilize """ no inicio e no fim
print('-------------------------------------------')
frase8= '        Curso em Video Python          '
print(frase.upper().count('o')) #frase.upper joga para maiuscula e .count conta a repetição
print(len(frase8)) #Muito utilizado para ver o tamanho da frase
print(len(frase8.strip())) #Remove os espaços vazios no começo e fim da frase
print('-----------------------------------------------------')
frase9= 'Curso em Video Python'
print(frase.replace('Python', 'AnDrOiD')) #.replace troca a palavra desejada na frase
print('---------------------quase----------------------')
frase10= 'Curso em Video Python'
print('Curso' in frase) #o in nos mostra se o que digitamos está ou não na frase com V ou F
print('--------------------------------------------------')
frase11= 'Curso em Video Python'
print(frase.find('Python')) #Busca a posição inicial de determinada palavra 
print('----------------Em lista---------------------')
frase12= 'Curso em Video Python'
print(frase.split()) #.split separa a frase em novas repartições partindo dos espaços entre elas
print('--------------------=FIM DA AULA (DESAFIOS)=----------------------')
nome= str(input('Qual o seu nome?')).strip() #.strip pode ser aplicado diretamente no imput
print('Analisando seu nome...aguarde...')
print ('Seu nome com letras maisculas fica assim: {}'.format(nome.upper()))
print ('Seu nome com letras minusculas: {}' .format(nome.lower())) #.Lower ao contrario de upper joga tudo para o minusculo
print('Seu nome tem ao todo {} letras' .format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('--------------------------------------------------')
num= int(input('Digite um numero:'))
n = str(num)
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
print('-------------------------------------------------------')
cid= str(input('Digite a cidade que nasceu:')).strip()
print(cid[:5].upper() == 'SANTO')
print('---------------------------------------------')
nome= str(input('Digite seu nome:')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())) #o in indicando a procura dentro da string
print('-------------------------------------------------')
frase15= str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes em sua frase'.format(frase15.count('A')))
print('A primeira letra A apareceu pela primeira vez na posição {}'.format(frase15.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase15.rfind('A')+1))
print('=========================================================')
print('----------|Aula finalizada, foi cansativo mas venci|-----------')