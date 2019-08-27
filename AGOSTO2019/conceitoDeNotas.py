# Aluno: Matheus da Silva Coimbra Patriota - 20192EWBJ0027
# Curso: Engenharia de Software

soma = 0
vermelho = 0
verde = 0
amarelo = 0
qntdAlunos = 0

def conceito(nota):
    if nota <= 10 and nota >= 8.5:
        print("seu conceito eh A")     
    elif nota < 8.5 and nota >= 7.0:
        print("seu conceito eh B")    
    elif nota < 7.0 and nota >= 5.0:
        print("seu conceito eh C")      
    elif nota < 5.0 and nota >= 3.0:
        print("seu conceito eh D")      
    else:
        print("seu conceito eh E")


while True:
  notaAluno = input("qual media o Aluno {:.0f} obteve esse periodo? ".format(qntdAlunos+1))
  if float(notaAluno) < 0:
    break
  elif float(notaAluno) < 0 or float(notaAluno) > 10:
      print("Numero invalido")
  else:
    if float(notaAluno) >= 7.0:
      conceito(float(notaAluno))
      verde +=1
    elif float(notaAluno) < 7.0 and float(notaAluno)>= 3.0:
      conceito(float(notaAluno))
      amarelo +=1
    elif float(notaAluno) < 3.0 :
      conceito(float(notaAluno))
      vermelho +=1
    soma += float(notaAluno)
    qntdAlunos +=1

# media alunos
media = soma / qntdAlunos

print()
print("A média dos Alunos é {:.1f}, e conceito".format(media))
conceito(media)
print()
print("A quantidade de Alunos Aprovados é {:.0f}".format(verde))
print()
print("A quantidade de Alunos na final é {:.0f}".format(amarelo))
print()
print("A quantidade de Alunos Reprovados é {:.0f}".format(vermelho))