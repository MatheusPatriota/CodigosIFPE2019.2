# Matheus da Silva Coimbra Patriota
# 20192EWBJ0027


arquivoEntradas = open("entradas.txt","r")
produto = 1

for i in arquivoEntradas.readlines():
    produto *= int(i)

arquivoEntradas.close()

arquivoSaida = open("saida.txt",'w')
arquivoSaida.write(str(produto))

arquivoSaida.close()