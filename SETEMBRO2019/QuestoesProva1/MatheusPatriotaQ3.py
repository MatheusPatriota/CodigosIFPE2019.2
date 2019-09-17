# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# sequencia de numeros inteiros
# para quando o numero digitado for negativo
# deve imprimir na ordem 
# a. quantidade total de numero lidos
# b. o maior e o menor numero lido
# c. a media de todos os numero lidos
# d. quantidade de numeros multiplos de 6
# e. media aritimetrica dos dois ultimos numeros digitados


# variaveis
totalDeNumeros = 0
maior = 0
menor = 0
soma = 0
ultimo = 0
penultimo = 0
multiplosDe6 = 0

# inicio da lógica
print()
print("** Bem vindo - vamos começar **")
while (True):
  numero = int(input("Digite um numero: "))
  # caso de parada
  if numero < 0:
    break
  # setando variaveis iniciais
  if totalDeNumeros <1:
    maior = numero
    menor = numero
    ultimo = numero
  
  else:
    # checa menor e maior
    if numero >= maior:
      maior = numero
    elif numero <= menor:
      menor = numero
    
    # caso para ultimo e penultimo
    if totalDeNumeros >= 1:
      penultimo = ultimo
      ultimo = numero
  
    # logica para multiplos de 6
    if(numero % 6 == 0):
      multiplosDe6 += 1

  soma += numero
  totalDeNumeros += 1

print()
print(("** essas são as saidas **").title())
print("A quantidade total de numeros lidos é: {:}".format(totalDeNumeros))
print("O maior número lido foi: {:}".format(maior))
print("O menor número lido foi: {:}".format(menor))
print("A média de todos os números lido é: {:0.0f}".format((soma/totalDeNumeros)))
print("A quantidade de multiplos de 6 é: {:}".format(multiplosDe6))
print("A média aritimétrica dos dois ultimos números digitados é: {:0.1f}".format((penultimo + ultimo) / 2))