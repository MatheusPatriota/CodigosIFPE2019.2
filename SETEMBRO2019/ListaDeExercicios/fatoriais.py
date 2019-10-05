# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# funcao fatorial
def fatorial(n):
  if n == 1:
    return 1
  return n * fatorial(n-1)

# variaveis
listaFatoriais = []
entrada = int(input("Informe um numero: "))

# amazenar o resultado dos fatoriais na lista
for i in range(entrada):
  listaFatoriais.append(fatorial(i+1))

# fazer a leitura e impressão dos elementos da lista
for i in range(len(listaFatoriais)):
  if i == len(listaFatoriais)-1:
    print("{:}".format(listaFatoriais[i]))
  else:
    print("{:}, ".format(listaFatoriais[i]), end="")

