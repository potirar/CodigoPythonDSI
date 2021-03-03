'''from os import system
system('cls')

print('*'*10,'EXEMPLO 1','*'*10)

valor = 1

while valor <= 10:
    print(valor)
    valor += 1
print('\n\n')

print('*'*10,'EXEMPLO 2','*'*10)


while True:
    num = int(input('Informe um valor qualquer:'))

    if num == 0:
        break #termina o programa'''

pessoas = []
for i in range(0, 5):
    pessoa = []
    pessoa.append(input('Informe a idade da pessoa: '))
    pessoa.append(input('Informe a altura da pessoa: '))
    pessoas.append(pessoa)

pessoas.reverse()
for pessoa in pessoas:
    print ('Idade: %s - Altura: %s' % (pessoa[0], pessoa[1]))

