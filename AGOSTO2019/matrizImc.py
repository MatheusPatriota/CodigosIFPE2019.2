import numpy as np

# 17 linhas
# 11 colunas


def calculoIMC(a, p):
    imc = p / (a**2)
    return round(imc,2)


coluna = np.arange(1.5, 2, 0.05)
linha = np.arange(50, 135, 5)
matriz = np.empty((17, 10), dtype=float)


for i in range(17):
    for j in range(10):
        imc = calculoIMC(coluna[j], linha[i])
        matriz[i][j] = imc

print(matriz)
# print(coluna)
# print(linha)
# print(matriz)
