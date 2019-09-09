# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software


# Um funcionário recebe um salário fixo mais 4% de comissão sobre o valor das suas vendas realizadas. Faça um programa que receba o salário fixo do funcionário e o valor das vendas, calcule e mostre seu salário final.

salarioFixo = float(input("Digite seu salário fixo: "))
valorDasVendas = float(input("Digite o valor das vendas: "))

#  valor final  é salario fixo mais 4% de comissao das vendas
valorFinaSalario = salarioFixo + (valorDasVendas * 0.04)

# exibicao 
print("O valor final do seu salário é de: {:0.2f}".format(valorFinaSalario))
