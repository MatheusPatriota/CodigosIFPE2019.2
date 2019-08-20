def calculoIMC(a, p):
    imc = p / (a**2)
    return imc


def saidaIMC(imc):
    if imc >= 40:
        print("Obesidade III(mórbida)")
    elif imc <= 39.99 and imc >= 35:
        print("Obesidade II (severa)")
    elif imc <= 34.99 and imc >= 30:
        print("Obsesidade I")
    elif imc <= 29.99 and imc >= 25:
        print("Acima do peso.")
    elif imc <= 24.99 and imc >= 18.5:
        print("Peso Normal")
    elif imc <= 18.49 and imc >= 17:
        print("Abauxi do peso")
    else:
        print("Muito abaixo do peso")


print("Calculadora do Indice de Massa Corporea(IMC)\n ")
altura = float(input("digite sua altura (em metros ex:1.71): "))
peso = float(input("digite seu peso (em quilogramas): "))

imc = calculoIMC(altura, peso)
saidaIMC(imc)
