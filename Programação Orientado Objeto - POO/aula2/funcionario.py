class Funcionario:
    #CRIANDO UM MÉTODO CONSTRUTOR
    #COMANDO INITI SERVE PARA COMMIT

    def __init__(self,nome,cargo,salario=1100):
        
        self.nome = nome
        self.funcao = cargo
        self.sal = salario
    

    def relatorio(self):
        print(f"Nome: {self.nome}, Cargo: {self.funcao}, Salário: {self.sal}")

'''
fulano = Funcionario('Roberto','Padeiro',1100)
fulano.relatorio()
'''