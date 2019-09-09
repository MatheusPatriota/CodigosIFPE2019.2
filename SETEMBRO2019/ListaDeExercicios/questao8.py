# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software


# reajuste salarial, recebe o salario e de acordo com o valor reajusta
# ate  300   50%
# entre 301 e 500 40%
# entre 501 e 700 30%
# entre 701 e 800 20%
# entre 801 e 1000 10%
# acima de 1000 5%

# entrada
salario = float(input("Digite o valor do seu salario atual: "))

# condicionais
if(salario > 0 and salario <= 300):
  newSalario = salario + (salario * 0.5)
  print("Seu novo salario é: {:0.2f}".format(newSalario))
elif (salario >300 and salario <= 500):
  newSalario = salario + (salario * 0.4)
  print("Seu novo salario é: {:0.2f}".format(newSalario))
elif (salario >500 and salario <= 700):
  newSalario = salario + (salario * 0.3)
  print("Seu novo salario é: {:0.2f}".format(newSalario))
elif (salario >700 and salario <= 800):
  newSalario = salario + (salario * 0.2)
  print("Seu novo salario é: {:0.2f}".format(newSalario))
elif (salario >800 and salario <= 1000):
  newSalario = salario + (salario * 0.1)
  print("Seu novo salario é: {:0.2f}".format(newSalario))
elif (salario >1000):
  newSalario = salario + (salario * 0.05)
  print("Seu novo salario é: {:0.2f}".format(newSalario))
else: 
  print("Salario não pode ser menor que zero!")