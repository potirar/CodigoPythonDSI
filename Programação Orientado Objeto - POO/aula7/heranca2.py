class Pessoa: #SUPERCLASSE
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__ #PEGA O NOME DA CLASSE

    def mostraClasse(self):
        print(f"{self.nomeClasse} = seu nome é {self.nome}")

class Aluno(Pessoa): #SUBCLASSE
    def __init__(self,nome,idade,matricula):
        Pessoa.__init__(self,nome,idade)
        self.matricula = matricula

    def mostraAluno(self):
        print(f"{self.nomeClasse} = sou estudante e meu nome é {self.nome}")

class Professor(Pessoa):
    def __init__(self,nome,idade,salario):
        Pessoa.__init__(self,nome,idade)
        self.salario = salario
