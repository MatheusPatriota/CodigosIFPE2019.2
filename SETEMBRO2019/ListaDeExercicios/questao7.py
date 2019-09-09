# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software


# receba 2 numeros execute uma das operacoes e se digitada opcao errada exiba mensagem de erro e pare o programa

# a) o primeiro elevado ao segundo numero
# b) Raiz quadrada de cada numero
# c) Raiz cubica de cada um dos números

def exibeResultado(operacao,numero1,numero2):
  if (operacao == 'a'):
    elevadoAoSegundo = (numero1 ** numero2) 
    print("\nO primeiro numero elevado ao segundo é: {:0.0f}".format(elevadoAoSegundo))
  elif (operacao == 'b'):
    raiz1 = numero1 **(1/2)
    raiz2 = numero2 **(1/2)
    print("\nA raiz quadrada do primeiro numero é: {:0.0f}\nA raiz quadrada do segundo numero é : {:0.0f}".format(raiz1,raiz2))
  elif (operacao == 'c'):
    raiz1 = numero1 **(1/3)
    raiz2 = numero2 **(1/3)
    print("\nA raiz cúbica do primeiro numero é: {:0.0f}\nA raiz cúbica do segundo numero é : {:0.0f}".format(raiz1,raiz2))
  else:
    print("Operação não permitida!")

# entradas 
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

# Menu de operacoes
print("Bem vindo - Essas são as operações disponiveis:")
print("a) o primeiro elevado ao segundo numero ")
print("b) Raiz quadrada de cada numero")
print("c) Raiz cubica de cada um dos números")

print()
operacao = input("Qual a operaçao desejada: ")

exibeResultado(operacao,numero1,numero2)