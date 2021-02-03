from os import system
system('cls')

print('*'*10,'EXEMPLO 1','*'*10)

valor = 1

while valor <= 10:
    print(valor)
    valor += 1
print('\n\n')

print('*'*10,'EXEMPLO 2','*'*10)

num = 0

while True:
    num = int(input('Informe um valor qualquer:'))

    if num == 0:
        break #termina o programa
