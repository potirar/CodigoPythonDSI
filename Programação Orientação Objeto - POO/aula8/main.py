from polimorfismo import Pessoa, Aluno, Professor

#Pessoa
p1 = Pessoa("José Lima")
p1.cpf = '12345678912'
print(len(p1.cpf))
p1.exibirDado()
#aluno
aluno1 = Aluno("Joana",123,"Sistema de Informação")
aluno1.exibirDado()
#professor
prof = Professor("Marcos Frota",3478.76,40)
prof.exibirDado()