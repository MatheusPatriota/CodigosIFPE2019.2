import math

#  5000 alvos
#  6 circulos
#  diamentro do circulo maior sera dado pelo user
# convencionado em CM


def calculoAreaTotal(diametroMaior, percentual, saida):
    if diametroMaior <= percentual:
        return 0
    saida = calculoAreaCirculo(
        diametroMaior) + calculoAreaTotal(diametroMaior-percentual, percentual, saida)
    return saida


def calculoAreaCirculo(diametro):
    raio = diametro/2
    area = (math.pi * (raio**2))
    return area


diametroMaior = input("digite o diametro do maior circulo: ")
s = 0
percentualDeDiminuicao = float(diametroMaior) / 6
saida = calculoAreaTotal(float(diametroMaior), percentualDeDiminuicao, s)
print(
    "\no total de papelao a ser utilizado serah de {0:0.0f} cm²" .format(saida*5000))
