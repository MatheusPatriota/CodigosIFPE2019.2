# Aluno: Matheus da Silva Coimbra Patriota - 20192EWBJ0027
# Curso: Engenharia de Software

print("**** Piramide ****")

base = int(input("Qual a base da piramide? (min de 5, max de 29): "))
lista = []
inicio = (int(base/2))-1
fim = (int(base/2))+1


if base < 5 or base > 29:
  print ("Entrada invalida")
else:
  for i in range(base):
    lista.append(" ")

  print()

  # caso o numero seja par 
  # ex.: 6
  #    #
  #   ##
  #  ####
  # ######

  if base % 2 == 0:
    lista[int(base/2)] = "#"
    print(''.join(map(str,lista)))
    lista[inicio] = "#"
    inicio -=1
    print(''.join(map(str,lista)))
    for i in range(int(base/2)-1):
      lista[inicio] = "#"
      lista[fim] = "#"
      print(''.join(map(str,lista)))
      inicio -=1
      fim +=1

  # caso o numero da base seja impar
  # ex.: 5
  # 
  #   #
  #  ###
  # #####

  else:
    lista[int(base/2)] = "#"
    for j in range(int(base/2)+1):
      print(''.join(map(str,lista)))
      if j < int(base/2):
        lista[inicio] = "#"
        lista[fim] = "#"
        inicio -= 1
        fim += 1 