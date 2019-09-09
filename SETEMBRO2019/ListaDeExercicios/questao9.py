# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# receba o tipo de investimento e seu valor, recalcule para 1 mes 
# tipo 1 = 3%
# tipo 2 = 4%


# entrada 
print("** Investimentos **")
print("Tipo 1 - Poupança - 3% mes")
print("Tipo 2 - Fundo renda fixa - 4% mes")
tipoInvestimento = int(input("Qual o tipo de investimento você deseja realizar:"))

# condicionais
if (tipoInvestimento == 1):
  valorInvestimento = float(input("Qual valor você deseja investir:"))
  newValor = valorInvestimento + (valorInvestimento*0.03)
  print("Investimento tipo 1 - Poupança - 3% mes")
  print("Com o passar de um mês seu capital será de: {:0.0f}".format(newValor))
elif (tipoInvestimento == 2):
  valorInvestimento = float(input("Qual valor você deseja investir:"))
  newValor = valorInvestimento + (valorInvestimento*0.04)
  print("Investimento tipo 2 - Fundo renda fixa - 4% mes")
  print("Com o passar de um mês seu capital será de: {:0.0f}".format(newValor))
else:
  print("Tipo inválido!")