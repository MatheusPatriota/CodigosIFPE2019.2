# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# recebe 2 numeros
# 1 = media entre os numeros digitados
# 2 = diferenca entre o maior e menor
# 3 = Produtos entre os numeros
# 4 = divisao do primeiro pelo segundo, sendo o 2 != 0

def exibeResultado(operacao,numero1,numero2):
  if (operacao == 1):
    media = (numero1 + numero2) / 2
    print("\nA media entre os numero é: {:0.0f}".format(media))
  elif (operacao == 2):
    if (numero1 >= numero2):
      diferenca = numero1 - numero2
      print("\nA diferença entre os numero é: {:0.0f}".format(diferenca))
    else:
      diferenca = numero2 - numero1
      print("\nA diferença entre os numero é: {:0.0f}".format(diferenca))
  elif (operacao == 3):
    produto = numero1 *  numero2
    print("\nO produto entre os numero é: {:0.0f}".format(produto))
  elif (operacao == 4):
    if(numero2 == 0):
      print("Divisão por zero não permitida")
    else:
      divisao = numero1 / numero2
      print("\nA divisão entre os numero é: {:0.0f}".format(divisao))
  else:
    print("Operação não permitida!")

  

# entradas 
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

# Menu de operacoes
print("Bem vindo - Essas são as operações disponiveis:")
print("1 - Media entre os numeros digitados ")
print("2 - Diferenca entre o maior e menor")
print("3 - Produto entre os numeros")
print("4 - Divisao do primeiro pelo segundo")
print()
operacao = int(input("Qual a operaçao desejada: "))

# chamada da funcao que contem as condicoes
exibeResultado(operacao,numero1,numero2)
