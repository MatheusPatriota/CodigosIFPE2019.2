# Matheus da Silva Coimbra Patriota
# 20192EWBJ0027

# variaveis
# transformando strings Maiusculas em strings Minusculas com compreensao de listas
listaStrings = ["Matheus", "Rafaela", "Jairzinho", "TODAS", "POLI"]
print(*listaStrings)
# Lógica sem compreensao de lista
# for i in range(len(listaStrings)):
#     listaStrings[i] = listaStrings[i].lower()

# Lógica com compreensao de listas
listaStrings = [elem.lower() for elem in listaStrings]
print(*listaStrings)

# devolve uma lista contendo apenas os números da lista original que são divisíveis por 7
# variaveis 
listaNumeros =  [1,2,7,14,21,25,24,36]
divisiveisPorSete = []

print(*listaNumeros)
# Lógica sem compreensao de lista
# for num in listaNumeros:
#     if num % 7 == 0:
#         divisiveisPorSete.append(num)

# Lógica com compreensao de listas
divisiveisPorSete = [num for num in listaNumeros if num % 7 == 0]
print(*divisiveisPorSete)