# autor: Matheus da Silva Coimbra Patriota
# curso: Engenharia de Software

# funcao de impressao de matrizes
def imprimeMatriz(matriz):
    for i in matriz:
        print (i)

# variables
matriz1 = [[1,2],[3,4]]
matriz2 = [[5,6],[7,8],[9,10],[11,12]]
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

# matrizes tamanhos iguais
if matrizMaior == None:
    for i in range(len(matriz1)):
        coluna = []
        for j in range(len(matriz1[0])):
            elem1 = matriz1[i][j]
            elem2 = matriz2[i][j]
            coluna.append(elem1 + elem2)

        matrizFinal.append(coluna)
# matrizes tamanhos diferentes
else:
    for i in range(len(matrizMaior)):
        if i >= len(matrizMenor):
            matrizFinal.append(matrizMaior[i])
        else:
            coluna = []
            for j in range(len(matriz1[0])):
                elem1 = matriz1[i][j]
                elem2 = matriz2[i][j]
                coluna.append(elem1 + elem2)

            matrizFinal.append(coluna)

# # compreensao de lista
# if matrizMaior == None:
#     matrizFinal = [[elemento for x in matriz1[0]] for elemento in matriz1]
# saidas  
print("A matriz um é:")
imprimeMatriz(matriz1)
print("A matriz dois é:")
imprimeMatriz(matriz2)
print("A soma das matrizes é:")
imprimeMatriz(matrizFinal)
