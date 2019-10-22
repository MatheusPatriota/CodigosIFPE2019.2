# Desafio 3 
# um dregrau tem 30 cm de largura
# quantos degraus sao necessarios para atingir a altura do prego


def calculaQntDegraus(alt):
    umDegrau = 0.3
    qntDegraus = 0
    somatorio = 0
    while somatorio < alt:
        qntDegraus = qtdDegraus + 1
        somatorio = somatorio + 0.3
    
    return qntDegraus

alturaDoPrego = input("a que altura esta o prego? (em metros)")

qntDegraus = calculaQntDegraus(float(alturaDoPrego))

print("A quantidade de degraus necessaria para chegar ate o local do prego eh de: {0:0.0f}" .format(qntDegraus))



