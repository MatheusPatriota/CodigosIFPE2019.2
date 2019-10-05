# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

import math

print("Descubra se o número é primo")
print()
numero = int(input("Informe um numero e veja se ele é primo ou não: "))
cond = False

# Lógica linear
# 2 -> n-1
for i in range(2,numero):
  if numero % i == 0:
    cond = True
    break

if cond == True:
  print("O número {:} não é Primo".format(numero))
else:
  print("O número {:} é Primo".format(numero))


