def calculaSen(catop,hip):
    if(checaZero(catop,hip) == 1):
        return 0
    else:
        x = catop / hip
        print ("Sen: " + str(x))

def calculaCos(catad,hip):
    if(checaZero(catad,hip) == 1):
        return 0
    else:
        x = catad / hip
        print ("Cos: " + str(x))

def calculaTag(catop,catad):
    if(checaZero(catop,catad) == 1):
        return 0
    else:
        x = catop / catad
        print ("tg: " + str(x))

def checaZero(a,b):
    if (a == 0 or b == 0):
        return 1

print("\nBem vindo, vamos calcular as informacoes de um triangulo retangulo")
catetoop = input("Insira o cateto oposto: ")
catetoad = input("Insira o cateto adjacente: ")
hip = input("Insira a hipotenusa: ")

calculaSen(int(catetoop),int(hip))
calculaCos(int(catetoad),int(hip))
calculaTag(int(catetoop),int(catetoad))

