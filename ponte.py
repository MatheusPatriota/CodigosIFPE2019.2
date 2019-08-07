# o comprimento da ponte eh fornecido em KM entre 2 - 4
# tera 4 hastes de sustentacao
# 1/20 da extensao da ponte 
# 5 cabos de aco por haste


def calculaQuantidadeCabosMetros(c):
    equi = c / 5
    temp = c
    saida = 0
    while temp > 0:
        saida += temp 
        temp -= equi
    saida = saida *4
    print ("\nO total de metros de cabo de aco necessario eh {0:0.0f}".format(saida) )


# trabalhar com conversoes em metros
while True:  
    extensao = input("Qual serah a extensao da ponte ? (Deve ser entre (2 - 4) KM): ")
    if(int(extensao) >=2 and int(extensao) <=4):  
        break  


alturaHaste = (int(extensao) * (1/20)) * 1000
comprimentoMaiorCabo = (int(extensao) / 2 ) * 1000
# 1000/5 = 200

calculaQuantidadeCabosMetros (comprimentoMaiorCabo)

