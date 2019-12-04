# Aluno: Matheus da Silva Coimbra Patriota
# Curso: Engenharia de Software

alunos = []

# Supomos que inicialmente o aluno nao tem disciplinas cursadas.
def inserir(cpf, nome) :
  alunos.append((cpf, nome, []))

def estaRegistrado(cpf) :
  l = [aluno for aluno in alunos if cpf in aluno]
  if len(l) > 0 :
    return l[0]
  return ()
  
"""  for (cpf, nome, disciplinas) in alunos :
    if cpfBuscado == cpf :
      return (cpf, nome, disciplinas) # True
  return ()    # False
"""

def removerAlt(cpf) :
  aluno = estaRegistrado (cpf)
  if aluno != () :
    alunos.remove(aluno)
    
#(cpf, nome, disciplinas)
def cadastrarDisciplina(cpf, codigo, nomeDisciplina,semestre) :
  aluno = estaRegistrado(cpf)
  if aluno != () :
    aluno[2].append((codigo, nomeDisciplina, semestre))
    
def jaCursou(cpf, codigo) :
  resultado = False
  aluno = estaRegistrado(cpf)
  if aluno != () :
    for x in aluno[2] :
      if x[0] == codigo :
        resultado = True
  return resultado

"""
def remover(cpf) :
  i = 0
  while i < len(alunos) :
    if alunos[i][0] == cpf :
      del alunos[i]
    i = i + 1

"""

# Iniciando o Programa

cpf = None
nomeAluno = None
listaDisciplinas = None


while True:

    print("----------------------------------------------")
    print("| Bem vindo ao Sistema de Cadastro de Alunos |")
    print("----------------------------------------------")
    print("| Operações disponiveis:                     |")
    print("| 1- Cadastrar Aluno                         |")
    print("| 2- Vincular Disciplina                     |")
    print("| 3- Remover Aluno                           |")
    print("| 4- Sair do Programa                        |")
    print("----------------------------------------------")
    operacao = int(input("Informe sua escolha: "))

    if operacao == 4:
        print("Finalizando o programa.")
        break
    elif operacao == 1:
        print("----------------------------------------------")
        print("| Bem vindo ao Sistema de Cadastro de Alunos |")
        print("----------------------------------------------")
        print("| Operações Selecionada: Cadastro de Alunos  |")
        print("----------------------------------------------")
        cpf = input("Iforme o cpf  do aluno:")
        if estaRegistrado(cpf):
            print("Desculpe, aluno já está registrado!")
        else:
            nomeAluno = input("Informe o nome do Aluno: ")
            inserir(cpf,nomeAluno)
            print("Aluno Registrado com Sucesso!")
          
    elif operacao == 2:
      print("----------------------------------------------")
      print("| Bem vindo ao Sistema de Cadastro de Alunos |")
      print("----------------------------------------------")
      print("| Operações Selecionada: Vincular Disciplina |")
      print("----------------------------------------------")
      cpf = input("Informe o CPF do aluno: ")
      if estaRegistrado(cpf):

        codDisciplina = input("Informe o codigo da disciplina: ")

        if jaCursou(cpf,codDisciplina):
          print("Usuario já cursou está disciplina!")
          
        else:
          nomedisciplina = input("Informe o nome da disciplina: ")
          semestre = input("Informe o semestre da disciplina: ")

          cadastrarDisciplina(cpf,codDisciplina,nomedisciplina,semestre)

          print("Disciplinas cadastradas com Sucesso!")


      else:
        print("Aluno não está Registrado, tente novamente!")
    elif operacao == 3:
      print("----------------------------------------------")
      print("| Bem vindo ao Sistema de Cadastro de Alunos |")
      print("----------------------------------------------")
      print("| Operações Selecionada: Remover Aluno       |")
      print("----------------------------------------------")
      cpf = input("Informe o CPF do aluno: ")

      if estaRegistrado(cpf):
        removerAlt(cpf)
      else:
        print("CPF inválido!")
