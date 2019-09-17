# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# variaveis
codigosProdutos = []
estoqueProduto = []

#  preenchimento da  lista
codigosProdutos = list(range(10))
for i in range(10):
  estoqueProduto.append(10) 

# logica 
print("** Bem vindo a Matheus store's **")
while (True):
  codigoCliente = int(input("Informe o código do cliente: "))
  if (codigoCliente == 0):
    break;
  else:
    codProd = int(input("Informe o codigo do produto: "))
    if(codProd in codigosProdutos):
      quantidadeProduto = int(input("informe a quantidade do produto: "))
      # pedido so pode ser atendido integralmente 
      if(estoqueProduto[codProd] >= quantidadeProduto):
        estoqueProduto[codProd] = estoqueProduto[codProd] - quantidadeProduto
        print("Pedido Atendido. Obrigado e volte sempre!")
      else:
        print("Não temos estoque suficiente dessa mercadoria.")
    else: 
      print("Código Inexistente.")  