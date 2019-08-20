def posicaoCoordenada(x, y):
    if x == 0 and y == 0:
        print("você está na origem")
    elif x == 0 and y > 0:
        print("você está no eixo y")
    elif x > 0 and y == 0:
        print("você está no eixo x")
    elif x > 0 and y > 0:
        print("você está no primeiro quadrante")
    elif x > 0 and y > 0:
        print("você está no quarto quadrante")
    elif x < 0 and y > 0:
        print("você está no segundo quadrante")
    else:
        print("você está no terceiro quadrante")


x = float(input("entre com o valor de X: "))
y = float(input("entre com o valor de Y: "))

posicaoCoordenada(x, y)
