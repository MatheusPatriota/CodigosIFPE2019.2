

def maiorDeTres(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("o maior numero é {}".format(num1))
    elif num2 > num1 and num2 > num3:
        print("o maior numero é {}".format(num2))
    else:
        print("o maior numero é {}".format(num3))


def main():
    print("Digite tres numeros, e te direi qual eh o maior\n")
    numero1 = input("digite um numero: ")
    numero2 = input("digite o segundo numero: ")
    numero3 = input("digite o terceiro numero: ")
    maiorDeTres(numero1, numero2, numero3)


main()
