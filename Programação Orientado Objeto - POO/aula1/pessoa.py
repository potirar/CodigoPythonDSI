from datetime import date

class Pessoa:
    # Atributos
    nome = "José"
    idade = 45
    altura = 1.78

    # Métodos

    def falar(self, texto): #self: diz a respeito a classe a qual está inserido.
        print("Hello World!") #primeiro parâmetro com self
        print(texto)
    
    def ouvir(self, som):
        print(som)
    
    def calculaAno(self,idade):
        anoAtual = date.today().year
        print(f'Você nasceu no ano de {anoAtual - idade}')


