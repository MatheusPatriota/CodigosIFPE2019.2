# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software


# recebo codigo do produto e quantidade
# calculo valor total, e dou o desconto 
# exibo o valor total
# 1 - 10 -> 10.00
# 11 - 20 -> 15.00
# 21 - 30 -> 20.00
# 31 - 40 -> 30.00
# ate 250.00 - 5%
# entre 250.00  e 500.00 - 10 %  
# acima de 500.00 - 15%

# entrada
codigo = int(input("Digite o codigo da mercadoria: "))
quantidade = int(input("Digite a quanditdade dos produtos: "))

precoSemDesconto = 0
cond = True

# condicionais para os codigos e precos
if (codigo >= 1 and codigo <= 10):
  precoSemDesconto = 10 * quantidade
elif (codigo > 10 and codigo <=20):
  precoSemDesconto = 15 * quantidade
elif (codigo > 20 and codigo <= 30):
  precoSemDesconto = 20 * quantidade
elif (codigo > 30  and codigo <= 40):
  precoSemDesconto = 30 * quantidade
else:
  print("Codigo invalido!")
  cond = False

# condicionais descontos
if (cond):
  if (precoSemDesconto <= 250):
    precoComDesconto = precoSemDesconto - (precoSemDesconto * 0.05)
    print("O valor a ser pago é: {:0.1f}".format(precoComDesconto))
  elif (precoSemDesconto > 250 and precoSemDesconto <= 500):
    precoComDesconto = precoSemDesconto - (precoSemDesconto * 0.1)
    print("O valor a ser pago é: {:0.1f}".format(precoComDesconto))
  elif (precoSemDesconto > 500):
    precoComDesconto = precoSemDesconto - (precoSemDesconto * 0.15)
    print("O valor a ser pago é: {:0.1f}".format(precoComDesconto))
