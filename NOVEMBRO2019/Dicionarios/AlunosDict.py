# Aluno: Matheus da Silva Coimbra Patriota
# Curso: Engenharia de Software

import os

alunos = {}

# funcao para remover a quebra de linha
def removeQuebraLinha(lista):   
    for i in range(len(lista)):
        lista[i] = lista[i].replace('\n',"")
    return lista

# funcao para inserir o aluno no banco de dados
def inserir(cpf, nome) :
  alunos[cpf] = (nome, {})
  
  f = open("AlunosCadastrados/"+nome+".txt","w")
  f.write(cpf+"\n")
  f.write(nome+"\n")

# funcao para checar se o aluno ja esta registrado
def estaRegistrado(cpf) :
  if cpf in alunos :
    return alunos[cpf]
  return ()

# funcao para remover aluno cadastrado
def remover(cpf) :
  if cpf in alunos :
    del alunos[cpf]

# funcao para cadastrar disciplina para determinado aluno
def cadastrarDisciplina(cpf, codigo, nomeDisciplina,semestre) :
  aluno = estaRegistrado(cpf)
  if aluno != () :
    disciplinasCursadas = aluno[1]
    disciplinasCursadas[codigo] = (nomeDisciplina, semestre)
    
# funcao para checar se o aluno ja cursou a disciplina
def jaCursou(cpf, codigo) :
  cursou = False
  aluno = estaRegistrado(cpf)
  if aluno != () and codigo in aluno[1] : 
    cursou = True
  return cursou

# funcao para remover o ultimo
def removeUltimo(str) :
  if len(str) > 0 and str[len(str) - 1] == '\n':
    return str[0:len(str)-1]
  else :
    return str

# funcao para ler banco de dados
def lerBD(arquivo):
  f = open(arquivo, 'r',encoding="latin-1")
  conteudo = f.readlines()
  bdAlunos = {}
  temp = []
  for x in conteudo :
    temp.append(removeUltimo(x))

  conteudo = temp
    
  i = 0
  while i < len(conteudo) :
    
    if (i + 2  < len(conteudo)) :
      cpf = conteudo[i]
      nome = conteudo[i+1]
      bdAlunos[cpf] = (nome, {})
      qtdDisciplinas = int(conteudo[i+2])
      i = i + 3
      ultimaPosicao = (i + (qtdDisciplinas * 3)) - 1
      while i <= ultimaPosicao:
        codigoDisciplina = conteudo[i]
        nomeDisciplina = conteudo[i+1]
        semestreDisciplina = conteudo[i+2]
        bdAlunos[cpf][1][codigoDisciplina] = (nomeDisciplina, semestreDisciplina)
        i = i + 3
    elif i < 2:
      cpf = conteudo[i]
      nome = conteudo[i+1]
      bdAlunos[cpf] = (nome, {})
      break

  f.close()     
  return bdAlunos

# funcao para imprimir os alunos cadastrados
def imprimeAlunos(dic):
  for i in dic:
    print("CPF: " + i)
    print ("Aluno: " + dic[i][0])
    print()

# funcao para remover aluno cadastrado
def removeAluno(cpf):
  del alunos[cpf]

# carrega o banco de dados
lista = os.listdir("AlunosCadastrados")
for i in lista:

  aluno = lerBD("AlunosCadastrados/"+i)
  for j in aluno:
    alunos[j] = aluno[j]

# inicio do programa
while True:

    print("----------------------------------------------")
    print("| Bem vindo ao Sistema de Cadastro de Alunos |")
    print("----------------------------------------------")
    print("| Operações disponiveis:                     |")
    print("| 1- Cadastrar Aluno                         |")
    print("| 2- Vincular Disciplina                     |")
    print("| 3- Alunos Cadastrados                      |")
    print("| 4- Remover Aluno                           |")
    print("| 5- Sair do Programa                        |")
    print("----------------------------------------------")
    operacao = int(input("Informe sua escolha: "))

    # operacao de parada 
    if operacao == 5:
        print("Finalizando o programa.")
        break
    # operacao de cadastro de aluno
    elif operacao == 1:
        print("----------------------------------------------")
        print("| Bem vindo ao Sistema de Cadastro de Alunos |")
        print("----------------------------------------------")
        print("| Operações Selecionada: Cadastro de Alunos  |")
        print("----------------------------------------------")
      
        cpf = input("Iforme o cpf  do aluno:")

        # checa se aluno ja esta registrado
        if estaRegistrado(cpf):
            print("Desculpe, aluno já está registrado!")
        else:
            # enquanto o cpf nao estiver de acordo com o padrao desejado
            while len(cpf) <11 or not cpf.isdigit():
              print("CPF deve conter 11 numeros ex.:(11111111111), tente novamente!")
              cpf = input("Iforme o cpf  do aluno:")

            nomeAluno = input("Informe o nome do Aluno: ")
            inserir(cpf,nomeAluno)
            print("Aluno Registrado com Sucesso!")
    
    # operacao de vinculo de disciplina
    elif operacao == 2:
      print("----------------------------------------------")
      print("| Bem vindo ao Sistema de Cadastro de Alunos |")
      print("----------------------------------------------")
      print("| Operações Selecionada: Vincular Disciplina |")
      print("----------------------------------------------")
      print("| Alunos Cadastrados:                        |")
      print("----------------------------------------------")
      imprimeAlunos(alunos)
      print("----------------------------------------------")

      cpf = input("Informe o CPF do aluno: ")
      
      if estaRegistrado(cpf):

        codDisciplina = input("Informe o codigo da disciplina: ")

        if jaCursou(cpf,codDisciplina):
          print("Usuario já cursou está disciplina!")
          
        else:
          numDisciplinasCursada = None
          nomedisciplina = input("Informe o nome da disciplina: ")
          semestre = input("Informe o semestre da disciplina: ")

          cadastrarDisciplina(cpf,codDisciplina,nomedisciplina,semestre)

          # atualizando BD
          f = open("AlunosCadastrados/"+alunos[cpf][0]+".txt","r")
          f = f.readlines()
          # removendo \n
          f = removeQuebraLinha(f)

          # atualizando quantidade de disciplinas cursadas
          if len(f) == 2:
            numDisciplinasCursada = 1
            f.append(numDisciplinasCursada)
            
          else:
            numDisciplinasCursada = int(f[2])
            numDisciplinasCursada += 1
            f[2] = numDisciplinasCursada
          
          f.append(codDisciplina)
          f.append(nomedisciplina)
          f.append(semestre)

          arq = open("AlunosCadastrados/"+alunos[cpf][0]+".txt","w")
          
          for i in f:
            arq.write(str(i)+"\n")

          arq.close()

          print("Disciplinas cadastradas com Sucesso!")

      else:
        print("Aluno não está Registrado, tente novamente!")

    # operacao de consulta do aluno
    elif operacao == 3:
      print("----------------------------------------------")
      print("| Bem vindo ao Sistema de Cadastro de Alunos |")
      print("----------------------------------------------")
      print("| Operações Selecionada: Alunos Cadastrados  |")
      print("----------------------------------------------")
      imprimeAlunos(alunos)
      print("----------------------------------------------")

      print("Deseja consultar as disciplinas de algum aluno?")
      print("1 - Sim")
      print("2 - Não")
      opcao =  int(input("Informe sua escolha: "))

      # caso queira consultar as diciplinas do aluno
      if opcao == 1:
        print()
        cpf = input("Informe o CPF do aluno: ")

        while not estaRegistrado(cpf):
          print("CPF inválido, por favor tente novamente!")
          cpf = input("Informe o CPF do aluno: ")
        
        if len(alunos[cpf][1]) == 0:
          print(alunos[cpf][0]+" não possui disciplinas cadastradas!")
          print()
        else:
          dic = alunos[cpf][1]
          nomeAlunoConsulta = alunos[cpf][0]
          chaves =  list(dic)

          print("----------------------------------------------")
          print("|          Consulta de disciplinas           |")
          print("----------------------------------------------")
          print("| " + "Aluno: " + nomeAlunoConsulta)
          print("| Código   -   Disciplina -   Semestre       |")
          
          for i in chaves:
            print("|    ", i, dic[i][0], dic[i][1])
          
            
          print()

    # operacao de remocao de aluno 
    elif operacao == 4:
      print("----------------------------------------------")
      print("| Bem vindo ao Sistema de Cadastro de Alunos |")
      print("----------------------------------------------")
      print("| Operações Selecionada: Remover Aluno       |")
      print("----------------------------------------------")
      print("| Alunos Cadastrados:                        |")
      print("----------------------------------------------")
      imprimeAlunos(alunos)
      print("----------------------------------------------")

      cpf = input("Informe o CPF do aluno: ")

      if estaRegistrado(cpf):
        os.remove("AlunosCadastrados/" + alunos[cpf][0] + ".txt")
        removeAluno(cpf)
        print("Alunos removido com Sucesso!")
        print()
      else:
        print("CPF inválido!")
