# Matheus da Silva Coimbra Patriota
# 20192EWBJ0027

def soma(a,b):
    return a + b

tupla = (1,2,3,4,6,9,25)

for i, j in enumerate(tupla):
    if i == 1:
        print("O segundo elemento da tupla é:",j)
    elif i == len(tupla)-2:
        print("O penultimo elemento da tupla é:",j)

soma = 0
newTupla = tupla[:4]
for i in newTupla:
    soma +=i
 
print("A soma dos 4 primeiros elementos da nova tupla é:", soma)
