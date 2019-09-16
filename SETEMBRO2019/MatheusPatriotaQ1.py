# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# cadastro de professor 
# Nome 
# idade
# salario 
# Nome de Disciplina
# usar title na saida


# entradas
print("** Bem vindo ao sistem de casdastro de professor **")
nomeDoProfessor = input("Informe o nome do professor: ")
idade = int(input("Informe a idade do professor: "))
salario = float(input("Informe o salário do professor: "))
nomeDisciplina = input("Informe o nome da Disciplina: ")

# juncao de todas as informacoes 
print()
print(("O nome do professor cadastrado é: {:},".format(nomeDoProfessor)).title())
print(("A idade do professor é: {:} anos,".format(idade)).title())
print(("O salário do professor é de: {:0.1f} reais,".format(salario)).title())
print(("A disciplina ministrada pelo professor é: {:}.".format(nomeDisciplina)).title())