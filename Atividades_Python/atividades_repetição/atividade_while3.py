numP = 1
numN = 0
soma = 0
for i in range(0,11):
    num = int(input('Informe um valor:'))
    if numP > 0:
        print(f'Número positivo{positivo}')
    elif numN < 0:
            print(f'Número negativo{negativo}')
            soma += num
    numP += 1
print(f'A soma dos número positivos são:{soma}')
print(f'A soma dos número negativos são:{numP}')
