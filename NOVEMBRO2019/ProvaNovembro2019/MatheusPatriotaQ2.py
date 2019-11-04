# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Curso: Engenharia de Software

# funcao para encontrar os elementos repetidos entre duas listas
def repetidosListas(lista1,lista2):
    # lista que irá armazenar os valores repetidos
    listaFinal = []
    # for para cada elemento da lista1
    for i in lista1:
        # for para cada elemento da lista2
        for j in lista2:
            # caso seja i e j sejam iguais o elemento está repetido 
            if i  == j:
                # se esse elemento ja esta na listaFinal, nao e necessario nova adicao na lista
                if not(i in listaFinal):
                    listaFinal.append(i);
                else:
                    continue
            else:
                continue
            
    return listaFinal

# variaveis de teste
l1 =[2, 3, 4, 5, 6, 7, 8]
l2 =[4,5,10,8,12,7,2]

saida = repetidosListas(l1,l2)
# impressao da saida
print(saida)
            
