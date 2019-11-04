def media(soma,qntPessoas):
    return soma / qntPessoas

contador = 1
menores380 = 0
numeroFilhos = 0
somaSalario = 0
maiorSalario = 0

while True:
    salario = float(input("Informe o salario da pessoa {:}: ".format(contador)))
    
    if salario == -1:
        break
    else:
        filhos = int(input("Informe a quantidade de filhos da Pessoa {:}: ".format(contador)))
        numeroFilhos += filhos
        somaSalario += salario
        
        if salario > maiorSalario:
            maiorSalario = salario
        if salario <380:
            menores380 +=1

        contador +=1

mediaSalarios = media(somaSalario,contador-1)
mediaFilhos = media(numeroFilhos,contador-1)
porcentagemMenores380 = (menores380 / (contador-1)) * 100

print()
print("Resultados: ")
print("O numero médio de filhos é de: {:0.2f}".format(mediaFilhos))
print("A média salarial é de: {:0.2f}".format(mediaSalarios))
print("O maior salário registrado foi de: {:0.2f}".format(maiorSalario))
print("A quantidade de Pessoas com salario inferior a 380 é de: {:0.2f} %".format(porcentagemMenores380))
