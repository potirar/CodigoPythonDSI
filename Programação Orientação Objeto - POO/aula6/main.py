from heranca import Pessoa, Aluno, Professor

#Instanciando objeto

p1 = Pessoa("Joaquim Lima",58)
a1 = Aluno("Patrícia Silva",34)
prof1 = Professor("Tomaz Galias",56)

'''
print(f"Pessoa: {p1.nome}")
print(f"Aluno: {a1.nome}")
print(f"Professor: {prof1.nome}")
'''

p1.mostraClasse()
a1.mostraAluno()
prof1.mostraProfessor()

