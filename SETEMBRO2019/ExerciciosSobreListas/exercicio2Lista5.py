# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software
# IMC

# variaveis
listaIMC  = []
mediaAltura = 0
mediaPeso = 0
mediaIMC = 0

# para 10 pessoas 
for i in range(10):
  # entradas primarias
  peso = float(input("Informe o peso da {:}º pessoa: ".format(i+1)))
  altura = float(input("Informe a altura da {:}º pessoa (ex.: 1.71): ".format(i+1)))

  # calculo imc
  imc = peso / (altura**2)
  # acrescendo valores
  mediaIMC += imc
  listaIMC.append(imc)
  mediaAltura += altura
  mediaPeso += peso

# calculando as medias
mediaAltura = mediaAltura / 10
mediaPeso = mediaPeso / 10
mediaIMC = mediaIMC / 10

# exibicao 
print()
print("** Exibição **")
for i in range(len(listaIMC)):
  print("O IMC da {:}ª pessoa é: {:0.2f}".format(i+1,listaIMC[i]))
print()
print("A média dos pesos é: {:0.1f}".format(mediaPeso))
print("A média das alturas é: {:0.1f}".format(mediaAltura))
print("A média de todos os IMC's é: {:0.1f}".format(mediaIMC))