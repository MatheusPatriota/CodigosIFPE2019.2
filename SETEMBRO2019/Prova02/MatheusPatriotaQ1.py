#Aluno: Matheus da Silva Coimbra Patriota 
# Matricula: 20192EWBJ0027
# Engenharia de Software

# variaveis 
nomesAlunos = []
cpfs = []
notas = []
contador = 0
faltosos = 0
contadorMaiorNota = 0
auxMaior = 0
soma = 0
media  = 0

print("** Bem vindo ao sistem de Cadastro de Alunos do IFPE **")

while(True):
  nomeAluno = input("Informe o nome do {}º Aluno: ".format(contador+1))
  if nomeAluno == "":
    break
  else:
    cpf = input("Informe o CPF do {}º Aluno: ".format(contador+1))
    nota = float(input("Informe a nota do {}º Aluno: ".format(contador+1)))
    contador += 1

    if nota >= 0 and nota <= 10:
      # armazenando valores na lista
      nomesAlunos.append(nomeAluno)
      cpfs.append(cpf)
      notas.append(nota)

      # soma para tirar a media
      soma += nota
    else:
      # faltosos
      faltosos += 1

# encontrando a maior nota
for i in range(len(notas)):
  if i == 0:
    auxMaior = notas[i]
    contadorMaiorNota = i
  else:
    if auxMaior < notas[i]:
      auxMaior = notas[i]
      contadorMaiorNota = i
    else:
      continue


# média aritmética
media = soma / (contador - faltosos)

# Saidas
print()
print("** Saídas **")
print("O número de faltosos foi de: {}.".format(faltosos))
print("O aluno que obteve a Maior nota foi {} com a nota de {}.".format(nomesAlunos[contadorMaiorNota],auxMaior))
print("A média aritmética dos Alunos foi de: {:0.2f}.".format(media))
print("")
   