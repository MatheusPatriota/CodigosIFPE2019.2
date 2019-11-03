# autor: Matheus da Silva Coimbra Patriota
# curso: Engenharia de Software
# matricula: 20192EWBJ0027
# baseaddo na explicação do professor Fabio Kon


# funcao de impressao de matrizes
def imprimeMatriz(matriz):
    for i in matriz:
        print (i)

def mat_mult(A, B):

    numLinhasA, numColunasA = len(A),len(A[0])
    numLinhasB, numColunasB = len(B),len(B[0])

    # garante que o numero de linha de A é igual ao numero de colunas B
    assert numColunasA == numLinhasB
    matrizResultante = []

    for linha in range(numLinhasA):
        # adicionando uma nova linha a matriz final
        matrizResultante.append([])
        for coluna in range(numColunasB):
            # adicionando uma nova coluna na linha
            matrizResultante[linha].append(0)
            for j in range(numColunasA):
                matrizResultante[linha][coluna] += A[linha][j] * B[j][coluna]
    
    return matrizResultante


A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

imprimeMatriz(mat_mult(A,B))