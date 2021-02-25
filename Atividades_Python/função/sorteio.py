from random import randint

def loteria(valor):
    aleatorio = randint(1,100)
    palpite = 1 #contador

    while valor != aleatorio:
        if valor > aleatorio:
            print("Informe um valor menor")
        elif valor < aleatorio:
            print("Informe um valor maior")
            palpite += 1
            valor = int(input("Informe o seu palpite: "))
    
    print(f"Parabéns você ganhou com o número {palpite} dos seu palpites")

numero = int(input("Informe um valor entre 1 a 100: "))
loteria(numero)
