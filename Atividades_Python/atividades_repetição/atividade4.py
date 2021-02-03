from os import system
soma = 0
for i in range(1, 11):
    idade = int(input(f'Informe a sua idade {i}:'))
    soma += idade

    system('cls')

media = soma/i

if media <= 25:
    print('turma jovem')
elif media > 25 and media <= 60:
    print('turma adulta')
elif media > 60:
    print('turma idosa')
print('\n\n')