# autor: Matheus da Silva Coimbra Patriota
# curso: Engenharia de Software

# variaveis
listStrings = []
finalList = []

# welcome
print("Bem Vindo ao programa de remoção de não-alfanumericos")
print("para encerrar a inserção de string, basta apertar enter")

# logic
while True:
    string = input(
        "Informe uma string qualquer(Uma string é um conjunto de caracteres): ")
    if string == "":
        break
    else:
        listStrings.append(string)

print("List before verification", *listStrings)

# no-alphanumeric remove
for element in listStrings:
    if (element.isalnum()):
        finalList.append(element)

print("List after verification", *finalList)
