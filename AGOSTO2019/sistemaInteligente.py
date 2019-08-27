# Aluno: Matheus da Silva Coimbra Patriota - 20192EWBJ0027
# Curso: Engenharia de Software

# adivinha que numero to pensando xD

comecoUser = int(input("Digite o inicio do intervalo: "))
fimUser = int(input("Digite o fim do intervalo: "))

lista = list(range(fimUser+1))
numero = int(fimUser/2)
comeco = comecoUser
fim = len(lista)

print("Pense em um numero entre {:} a {:} ".format(comeco,fim-1))
while True:
  entrada = input("Seu numero é maior, menor ou igual a {:} : ".format(numero))
  if entrada == "igual":
    print("Acertei xD")
    break
  elif entrada == "menor":
    lista = list(range(comeco,numero-1))
    fim = numero
    numero = lista[int(len(lista)/2)]
  elif entrada == "maior" and numero == 100:
    print("numero nao pode ser maior que 100")
  elif  entrada == "maior":
    lista = list(range(numero+1,fim))
    numero = lista[int(len(lista)/2)]
    comeco = lista[0]

