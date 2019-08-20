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


notaAluno = input("qual media voce obteve esse periodo? ")
if float(notaAluno) < 0 or float(notaAluno) > 10:
    print("Numero invalido")
else:
    conceito(float(notaAluno))
