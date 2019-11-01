# resposta do exercicio
perg1 = input("Telefonou? ")
perg2 = input("Esteve? ")
perg3 = input("Mora? ")
perg4 = input("Devia? ")
perg5 = input("Trabalhou? ")
contador = 0
lista = [perg1,perg2,perg3,perg4,perg5]

for i in lista:
    if i == "s":
        contador += 1

if contador == 2:
    print("Suspeito")
elif contador >=3 and contador <=4:
    print("Cumplice")
elif contador == 5:
    print("Assassino")
else:
    print("Inocente")