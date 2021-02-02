texto = 'Faz por ti e eu te ajudarei'
print('ajudarei' in texto)

for cont in range(10):
    print(cont)

for cont in range(1,10):
    print(cont,' ', end = '') #impedindo de quebrar linha'''

for cont in range(1,21,3): #o 3º parâmetro é o incremento dos valores
    print(cont)

for cont in range(11, 0, -1):
    print(cont,'', end='')

print('-'*15, 'VALORES PARES','-'*15)
for cont in range(1,11):
    if cont %2 == 0:
        print(cont,'',end = '')

