velocidade_permitida = float(input('Qual a velocidade permitida nesse trajeto:'))
velocidade_aferida = float(input('Qual a velocidade aferida no trajeto:'))

velocidade20 = (velocidade_permitida * 0.20) + velocidade_permitida
velocidade50 = (velocidade_permitida * 0.50) + velocidade_permitida

if velocidade_aferida <= velocidade_permitida:
    print('nao precisa')

elif velocidade_aferida > velocidade_permitida and velocidade_aferida <= velocidade20:
    print('Infração média')

elif velocidade_aferida > velocidade_permitida and velocidade_aferida <= velocidade50:
    print('Infração grave')

elif velocidade_aferida > velocidade50:
    print('infração gravissima')







 