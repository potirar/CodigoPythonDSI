class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        self.__cpf = ''

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,valor):

        if len(valor) != 11:
            print("ATENÇÃO!!!\nO CPF precisa conter 11 digitos e somente números")
        
        elif valor.isnumeric():
            self.__cpf = valor
        
        else:
            print('Insira apenas números')

    def exibirDado(self):
        print(f"Nome: {self.nome}")
        #print(f"CPF: {self.cpf}")
        
class Aluno(Pessoa):
    def __init__(self,nome,matricula,curso=''):
        super().__init__(nome) #PARÂMETRO SELF SÓ SERÁ PRECISO SE NÃO FOR USAR SUPER()
        self.matricula = matricula
        self.curso = curso

    def exibirDado(self):
        super().exibirDado()
        print(f'Matricula: {self.matricula}')
        print(f'Curso: {self.curso}')

class Professor(Pessoa):
    def __init__(self,nome,salario='',ch=''):
        super().__init__(nome)
        self.salario = salario
        self.ch = ch

    def exibirDado(self):
        super().exibirDado()
        print(f"Salário:R$ {self.salario}")
        print(f"Carga Horária: {self.ch} horas")

