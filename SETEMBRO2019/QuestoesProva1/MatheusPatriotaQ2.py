# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# ** FOI UTILIZADO UM ACRESCIMO A CADA 100 KILOWATTS **
# ** SE FOR MENOR QUE 100 KILOWATTS NÃO HAVERÁ ACRESCIMO **

# variaveis imutaveis
kwh = 0.04

# entradas 
print(("** Bem vindo ao calculo de conta de energia **").title())
quantidadeKWH = float(input("Informe a quantidade de quilowatts-hora consumidos por sua residência nesse mês: "))
print("Existem essas possibilidades de bandeira tarifária:")
print("1 - verde")
print("2 - amarela")
print("3 - vermelha patamar I")
print("4 - vermelha patamar II")
bandeira = input("Informe a bandeira desse mês: ")

valorTotal = 0
# checa a bandeira e acresce o valor caso necessario 
if bandeira == '1':
  valorTotal = quantidadeKWH * kwh
elif bandeira == '2':
  # dividir a quantidade de kWh por 100, peger a parte inteira e multiplicar pela tarifa
  if (quantidadeKWH / 100) < 1:
    valorTotal = quantidadeKWH * kwh
  else:
    temp = int(quantidadeKWH / 100)
    valorTotal = (quantidadeKWH *kwh) + (temp * 1.5)
elif bandeira == '3':
  if (quantidadeKWH / 100) < 1:
    valorTotal = quantidadeKWH * kwh
  else:
    temp = int(quantidadeKWH / 100)
    valorTotal = (quantidadeKWH *kwh) + (temp * 4.0)
elif bandeira == '4':
  if (quantidadeKWH / 100) < 1:
    valorTotal = quantidadeKWH * kwh
  else:
    temp = int(quantidadeKWH / 100)
    valorTotal = (quantidadeKWH *kwh) + (temp * 6.0)


# Casos de pagamento para dias diferntes
# antes antes do dia 10 - 8%
antesDia10 = valorTotal - (valorTotal * 0.08)
# entre dia 10 e 15
entre10E15 = valorTotal - (valorTotal * 0.05)
# depois dia 15, pago o valor total

# exibicao
print()
print(("** Esses são os valor que você poderá pagar dependendo do dia do pagamento **").title())
print("Caso você pague a conta antes do dia 10, você irá pagar: {:0.2f} reais".format(antesDia10))
print("Caso você pague a conta entre o dia 10 e o dia 15, você irá pagar: {:0.2f} reais ".format(entre10E15))
print("Caso você pague a conta depois do dia 15, você irá pagar: {:0.2f} reais".format(valorTotal))

