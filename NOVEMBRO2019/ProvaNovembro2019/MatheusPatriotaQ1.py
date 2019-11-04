# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Curso: Engenharia de Software

# funcao para encontrar os maiores elementos de cada linha da matriz
def maioresLinhaMatriz(matriz):
    # saida ira armazenas o maior valor de cade linha da matriz
    saida = []
    for i in matriz:     
        maior =  0
        for indice,elemento in enumerate(i):
            # setando o primeiro elemento como o maior
            if indice == 0:
                maior = elemento
            else:
                if elemento > maior:
                    maior = elemento
        # adicionando o maior elemento da linha na saida
        saida.append(maior)
    return saida


# variaveis de teste
matriz =  [[2,0,6],[3,1,9],[4,6,100],[12],[25,33]]
newMatriz = maioresLinhaMatriz(matriz)
# impressão da lista de maiores elementos
print(newMatriz)
