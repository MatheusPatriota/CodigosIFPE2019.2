soma = 0
media = 0
maior = 0
menor = 0
                               
for i in range(6):
  
  entrada = float(input("Insira o número: "))
  # pegando o primeiro elemento como o menor
  if (i == 0):
    menor = entrada
  #  soma 
  soma += entrada
  # maior
  if entrada > maior:
    maior = entrada
  # menor 
  elif entrada < menor:
    menor = entrada

# media 
media = soma / 6


print()
print("A soma é : {:.0f}".format(soma))
print("A média dos numeros é: {:.1f}" .format(media))
print("O maior número é: {:.0f}".format(maior))
print("O menor número é: {:.0f}".format(menor))