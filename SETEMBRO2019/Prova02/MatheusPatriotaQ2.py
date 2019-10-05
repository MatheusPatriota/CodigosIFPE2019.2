#Aluno: Matheus da Silva Coimbra Patriota 
# Matricula: 20192EWBJ0027
# Engenharia de Software

# variaveis
divisores = []
somaDivisores = 0

print("** Bem vindo ao Descubra se seu numero é perfeito ou não **")
numero = int(input("Informe um número para começar: "))

# listas para encontrar divisores do numero
for i in range(1,numero,1):
  if numero % i == 0:
    divisores.append(i)

# soma dos divisores
for j in divisores:
  somaDivisores += j

# checagem e impressão do resultado
if somaDivisores == numero:
  print("Perfeito!")
else:
  print("Não é perfeito!")