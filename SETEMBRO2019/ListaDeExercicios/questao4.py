# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software


# Faça um programa em Pascal que calcula o raio, o perímetro e a área de uma circunferência a partir do diâmetro digitado pelo usuário. Após realizar o cálculo, seu programa deve mostrar na tela o valor do raio, do  perímetro e da área da circunferência. 
#  Lembre-se que pi ~ 3,14. π = 3,14

# diametro da circunferência e valor de pi
diametro = float(input("Informe o valor do diâmetro da circunferência: "))
pi = 3.14

# raio da circunferência
raio = diametro / 2

# perimetro da circunferência
perimetro  = 2 * pi * raio

# area da circunferência
area = pi * (raio**2)

# exibicao
print("Para a circunferência com diametro de {:0.0f}".format(diametro))
print("Seu raio é: {:0.1f}".format(raio))
print("Seu Perimetro: {:0.1f}".format(perimetro))
print("Sua Area é de: {:0.1f}".format(area))