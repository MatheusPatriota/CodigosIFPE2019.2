# divisao sucessiva por 2
# desafio 4

def convertDecimalToBinary(decimal):
    binario = []
    aux = decimal
    saida = ""
    while aux > 1:
        resto = aux % 2
        binario.append(int(resto))
        aux = aux /2
    # lida com a lista de tras para frente ;)
    for x in binario[::-1]:
        saida += str(x)
        
    print("\no decimal {0:0.0f} em binario eh " .format(decimal) + saida)
        

numeroDecimal = input("Escreva um numero em Decimal: ")
convertDecimalToBinary(int(numeroDecimal))
