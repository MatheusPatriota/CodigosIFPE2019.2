# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software


# Faça um programa que recebe um valor em segundos. Converta o valor recebido para o formato HH:MM:SS,
# onde HH é a quantidade de horas, MM é a quantidade de minutos e SS é a quantidade de segundos. Lembre
# que 1 hora equivale a 60 minutos e a 3600 segundos. Lembre também que 1 minuto equivale a 60 segundos.


entradaEmSegundos = int(input("Informe a quantidade de Segundos: "))

# 1 hora tem 3600 segundos
horas = entradaEmSegundos / 3600
restoHoras = entradaEmSegundos % 3600
# 1 minuto tem 60 segundos
minutos = restoHoras / 60
restoMinutos = restoHoras % 60
segundos = restoMinutos


# exibicao 

# tranformando em string os valores obtidos
horaFinal = str(int(horas))
minutoFinal = str(int(minutos))
segundoFinal = str(int(segundos))

# para ficar no formato HH:MM:SS
if len(horaFinal) <2:
  horaFinal = '0' + str(int(horas))
if len(minutoFinal)  <2:
  minutoFinal = '0' + str(int(minutos))
if len(segundoFinal)  <2:
  segundoFinal = '0' + str(int(segundos))
  

# imprimindo na tela
print("{:}:{:}:{:}".format(horaFinal,minutoFinal,segundoFinal))