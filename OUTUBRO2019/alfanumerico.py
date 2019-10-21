# autor: Matheus da Silva Coimbra Patriota
# curso: Engenharia de Software

# variaveis
listStrings = ["matheus@123","rafa@#$","clenio"]
newStringList = []


# welcome
print("Bem Vindo ao programa de remoção de não-alfanumericos")
print("para encerrar a inserção de string, basta apertar enter")

# logic
# while True:
#     string = input(
#         "Informe uma string qualquer(Uma string é um conjunto de caracteres): ")
#     if string == "":
#         break
#     else:
#         listStrings.append(string)

print("List before verification", *listStrings)

# no-alphanumeric remove normal
for element in listStrings:
    string = ""
    for i in element:
        if (i.isalnum()):
            string += i
        
    newStringList.append(string)

# no-alphanumeric remove compreensao de listas

print("List after verification", *newStringList)
