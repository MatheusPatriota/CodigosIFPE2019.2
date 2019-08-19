import math
# Desafio 1
# o comprimento da ponte eh fornecido em KM entre 2 - 4
# tera 4 hastes de sustentacao
# 1/20 da extensao da ponte
# 5 cabos de aco por haste


def calculaQuantidadeCabosMetros(c):
    equi = c / 5
    temp = c
    saida = 0
    while temp > 0:
        saida += temp
        temp -= equi
    saida = saida * 4
    print(
        "\nO total de metros de cabo de aco necessario eh {0:0.0f}".format(saida))


def calculoHipotenusa(cat1, cat2):
    temp = (cat1**2) + (cat2 ** 2)
    hip = math.sqrt(temp)
    return hip


# trabalhar com conversoes em metros
while True:
    extensao = input(
        "Qual serah a extensao da ponte ? (Deve ser entre (2 - 4) KM): ")
    if(float(extensao) >= 2 and float(extensao) <= 4):
        break


alturaHaste = (float(extensao) * (1/20)) * 1000
comprimentoMaiorCabo = calculoHipotenusa(alturaHaste, (float(extensao)/2)*1000)
# 1000/5 = 200

calculaQuantidadeCabosMetros(comprimentoMaiorCabo)
