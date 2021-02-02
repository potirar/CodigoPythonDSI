peso = float(input('Infome seu peso:'))
altura = float(input('Informe a sua altura'))
imc = peso / altura ** 2
print('seu imc é:{:.2f}'.format(imc))

if imc < 16:
    print('magreza grave')

elif imc > 16 and imc <=17:
    print('magreza moderada')

elif imc > 17 and imc <=18.5:
    print('magreza leve')

elif imc > 18.5 and imc <=25:
    print('Saudavel')

elif imc >25 and imc <=30:
    print('Sobrepeso')

elif imc >30 and imc <=35:
    print('Obesidade grau I')

elif imc >35 and imc <= 40:
    print('Obesidade grau II')
    
elif imc > 40:
    print('Obsidade grau III')

