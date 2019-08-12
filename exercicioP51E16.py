import math


def calculoHip(c1, c2):
    x = math.sqrt((c1**2) + (c2**2))
    return x


cateto1 = input("digite o cateto: ")
cateto2 = input("digite o cateto: ")

hip = calculoHip(int(cateto1), int(cateto2))

print("a hipotenusa é: {0:0.1f}".format(hip))
