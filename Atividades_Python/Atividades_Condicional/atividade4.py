km = float(input('Quantos quilômetros o seu carro faz por litro?'))
restante = float(input('Quanto litros de gasolina há no momento em seu tanque?'))
trajeto = float(input('Quantos quilômetros você deseja pecorrer hoje?'))

if trajeto / km < restante:
    print('Tranquilidade meu chapa!')
else:
    print('Ferrou meu chapa, você precisa abastercer {:.2f} litros\n\n'.format(trajeto / km - restante))10


