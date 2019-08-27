# Aluno: Matheus da Silva Coimbra Patriota - 20192EWBJ0027
# Curso: Engenharia de Software

def calculoIMC(a, p):
    imc = p / (a**2)
    return imc

def saidaIMC(imc):
    if imc >= 40:
        return("Obesidade III(mórbida)")
    elif imc <= 39.99 and imc >= 35:
        return("Obesidade II (severa)")
    elif imc <= 34.99 and imc >= 30:
        return("Obsesidade I")
    elif imc <= 29.99 and imc >= 25:
        return("Acima do peso.")
    elif imc <= 24.99 and imc >= 18.5:
        return("Peso Normal")
    elif imc <= 18.49 and imc >= 17:
        return("Abaixo do peso")
    else:
        return("Muito abaixo do peso")


print("Calculadora do Indice de Massa Corporea(IMC)\n ")

soma = 0
for i in range(0,10):
  
  altura = float(input("digite a altura da pessoa {:.0f} (em metros ex:1.71): ".format(i+1)))
  peso = float(input("digite o peso da pessoa {:.0f}  (em quilogramas): ".format(i+1)))
  imc = calculoIMC(altura,peso)
  soma += imc
  conceito = saidaIMC(imc)

  print ("A pessoa {:.0f} tem o IMC de {:.2f}, e conceito {:}".format(i,imc,conceito))

# media das 10 pessoas  
media = soma / 10
# saida da media geral e conceito
print()
print ("A media de IMC é {:.2f}, e o conceito é".format(media),saidaIMC(media))