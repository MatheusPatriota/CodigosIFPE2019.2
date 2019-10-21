# Codigo representando listas
nomes = []
for i in range(3):
    nome = input("Informe um nome para lista: ")
    nomes.append(nome)

print(*nomes)