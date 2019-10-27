# Matheus da Silva Coimbra Patriota
# 20192EWBJ0027

import math

def soma(a,b):
    return a+b

# a = 2 b =-16 c = -18
def bhaskara(a,b,c):
    raiz = math.sqrt(b**2 - (4*a*c))
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    print ("x1:",x1,"; x2",x2)


a = int(input("informe o valor de A: "))
b = int(input("informe o valor de B: "))
c = int(input("informe o valor de C: "))

print("A soma de A + B é:",soma(a,b))
print("As raizes da função são: ")
bhaskara(a,b,c)