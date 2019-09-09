# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software


# recebe idade, peso e altura de 10 pessoas

# calcular a media das idades (caso A)
# quantas pessoas possuem mais de 70kg (caso B)
# media da altura das pessoas que possuem entre 12 e 21 anos (caso C)
# quantas pessoas possuem mais de mais que 90kg e menores que 1.80 (caso D)

# variaveis globais para uso na estrutura
mediaIdades = 0
quantidadePessoasPesoMaior70 = 0
quantidadePessoasPesoMaior90Menor180 = 0
mediaAlturaPessoas = 0
qntParaCasoC = 0

for i in range(10):
  # entradas
  idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
  peso  = float(input("Digite o peso da pessoa {}: ".format(i+1)))
  altura = float(input("Digite a altura da pessoa {} (ex.:1.80): ".format(i+1)))

  # tratamentos condicionais
  if(peso > 70.0):
    quantidadePessoasPesoMaior70 +=1
  if(idade >=12 and idade <=21):
    mediaAlturaPessoas += altura
    qntParaCasoC += 1
  if(peso > 90 and altura <1.80):
    quantidadePessoasPesoMaior90Menor180 += 1
  
  mediaIdades += idade


# exibicao 

mediaAlturaPessoas = mediaAlturaPessoas /qntParaCasoC
mediaIdades = mediaIdades /10

print("Resultados:")
print("Média das idades: {}".format(mediaIdades))
print("Quantidade de pessoas que possuem mais de 70kg: {:0.1f}".format(quantidadePessoasPesoMaior70))
print("Média da altura das pessoas que possuem entre 12 e 21 anos: {:}".format(mediaAlturaPessoas))
print("Quantidade de pessoas que possuem mais de 90kg e são menores que 1.80: {:0.2f}".format(quantidadePessoasPesoMaior90Menor180))