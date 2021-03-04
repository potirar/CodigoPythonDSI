class Conta:
    def __init__(self,numero,titular,saldo,limite=1000):
       
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposito(self,valor):

        if valor < 0:
            print("Você não pode depositar esse valor!")
        else:
            self.__saldo += valor
    
    def saque(self,valor):

        if valor > self.__saldo:
            print(f"Você não poderá sacar este valor, seu saldo é {self.__saldo}")
        else:
            self.__saldo -= valor
            print(f"Saque realizado com sucesso!")

    def getSaldo(self): #Exibindo saldo
        print(f"Seu saldo é {self.__saldo}")

# OUTRA FORMA DE CRIAR GETTERS E SETTERS

class Conta2:
    def __init__(self,numero,titular,saldo,limite=1000):
       
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #decorator
    #Exibir o saldo
    @property
    def saldo(self):
        return f"O seu saldo é R$ {self.__saldo}"

    #Definir valor para o atributo
    @saldo.setter
    def saldo(self,valor):
        if valor < 0:
            print(f"Você não pode depositar valores negativos")
        else:
            self.__saldo += valor
            print("Valor depositado com sucesso!")
       
