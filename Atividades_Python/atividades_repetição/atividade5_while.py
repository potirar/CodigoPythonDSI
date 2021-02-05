while True:
    valor = int(input('Informe um valor'))

    if valor < 0:
        break

    elif valor > 100:
        print('LIMITE EXCEDIDO!!!!')
    elif valor > 10:
        print(f'O quafrado de {valor} é {valor ** 2}:')
    elif valor > 5:
        print(f'O cubo do {valor} é {valor ** 3}')
