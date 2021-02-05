while True:
    num = int(input('Informe um valor:'))
    if num == 0:
        break
        if i == 0:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
        i += i
        