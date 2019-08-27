print("**** Piramide ****")

base = int(input("Qual a base da piramide? (min de 5, max de 29): "))
temp = 1
lista = []
inicio = (int(base/2))-1
fim = (int(base/2))+1


if base < 5 and base > 29:
  print ("Entrada invalida")
else:
  for i in range(base):
    lista.append(" ")

print()
lista[int(base/2)] = "#"

for j in range(int(base/2)+1):
  print(''.join(map(str,lista)))
  if j < int(base/2):
    lista[inicio] = "#"
    lista[fim] = "#"
    inicio -= 1
    fim += 1      