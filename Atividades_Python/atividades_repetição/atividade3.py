import time
import os

pessoas = int(input('Quantas pessoas querem se hospedar: '))
h = 0
m = 0

for i in range(0, pessoas):
    nome = input('Qual seu nome?')
    sexo = input('Qual o seu sexo? m/f:')

    if sexo == 'm':
        print(f'Bem vindo Sr. {nome}')
        h += 1
    else:
        print(f'Bem vindo Sra. {nome}')
        m += 1

        time.sleep(1)
        os.system('cls')
print(f'No quarto estão hospedados um total de {h} homens e {m} mulheres neste hotel')