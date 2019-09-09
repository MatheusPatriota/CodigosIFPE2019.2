# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# Faça um programa que calcula a média ponderada entre duas notas digitadas pelo usuário. Considere peso 3 para a primeira e peso 1 para a segunda nota.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# calculo da media ponderada
# (p1 * n1 + p2 * n2) / p1 + p2

mediaPonderada = (1 * nota1 + 3 * nota2)/ 4

# exibindo resultado 

print("A media ponderada das notas informadas é: {:0.1f}".format(mediaPonderada))
