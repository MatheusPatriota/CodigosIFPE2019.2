# autor: Matheus da Silva Coimbra Patriota
# curso: Engenharia de Software

# variables
matriz1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
matriz2 = [[91, 10], [11, 12], [13, 14], [15, 16]]
matrizMaior = None
matrizMenor = None
linha = []
coluna = []
matrizFinal = []


# logic
if len(matriz1) > len(matriz2):
    matrizMaior = matriz1
    matrizMenor = matriz2
elif len(matriz1) < len(matriz2):
    matrizMaior = matriz2
    matrizMenor = matriz1

if matrizMaior == None and matrizMenor == None:
    for i in range(len(matriz1)):
        coluna = []
        for j in range(len(matriz1[0])):
            elem1 = matriz1[i][j]
            elem2 = matriz2[i][j]
            coluna.append(elem1 + elem2)

        matrizFinal.append(coluna)


print(matriz1)
print(matriz2)
print(matrizFinal)

# for element in matrizMaior:
