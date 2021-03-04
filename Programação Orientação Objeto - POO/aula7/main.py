from heranca2 import Aluno, Professor

a1 = Aluno("Marta Silva",23,1678)
a1.mostraAluno()
print(f"A matrícula de {a1.nome} é {a1.matricula}\n")

prof1 = Professor("Geraldo",54,3600)
print(f"O salário de {prof1.nome} é {prof1.salario}")