# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# variaveis
lista = []
maior = 0
menor = 0
soma = 0
media = 0


for i in range(6):
  numero =  int(input("Informe um número: "))

  # logica para maior e menor
  # setando maior e menor para o primeiro numero
  if (i == 0):
    maior = numero 
    menor = numero
  
  if(numero > maior):
    maior = numero
  elif (numero < menor):
    menor = numero
  
  # soma dos numeros  
  soma += numero

  # adicionando na lista
  lista.append(numero)

# media
media = soma / 6

# exibicao 
print()
print("** Exibição **")
print("a. Os números informados foram:", lista)
print("b. A soma dos elementos é:", soma)
print("c. A média dos números informados é: {:}".format(media))
print("d. O maior número é:", maior)
print("e. O menor número é:", menor)
