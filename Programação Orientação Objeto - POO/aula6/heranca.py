#Trabalhando com herança simples
class Pessoa: #SUPERCLASSE
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__ #PEGA O NOME DA CLASSE

    def mostraClasse(self):
        print(f"{self.nomeClasse} = seu nome é {self.nome}")

class Aluno(Pessoa): #SUBCLASSE
    def mostraAluno(self):
        print(f"{self.nomeClasse} = sou estudante e meu nome é {self.nome}")

class Professor(Pessoa):
    def mostraProfessor(self):
        print(f"{self.nomeClasse} = sou professor e meu nome é {self.nome}")
