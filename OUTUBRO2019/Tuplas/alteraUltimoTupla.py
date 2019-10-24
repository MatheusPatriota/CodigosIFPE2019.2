listaTupla = [(1,2),(2,3),(4,5),(6,7),(8,9)]
listaFinal = []
for (x,y) in listaTupla:
    print (x,y)
    y = 0
    listaFinal.append((x,y))

print(*listaFinal)
