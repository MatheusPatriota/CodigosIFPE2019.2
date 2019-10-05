# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Engenharia de Software

# variaveis
codigosProdutos = []
estoquesProduto = []

#  preenchimento da  lista
codigosProdutos = list(range(10))
for i in range(10):
  estoquesProduto.append(10) 

# logica 
print("** Bem vindo a Matheus store's **")
while (True):
  codigoCliente = int(input("Informe o código do cliente: "))
  if (codigoCliente == 0):
    break;
  else:
    print("Bem vindo - Os produtos disponiveis para compra são: ")
    print("1 - Leite Integral")
    print("2 - Maminha da Vaquinha")
    print("3 - Carne de Touro")
    print("4 - Xucrute Integral")
    print("5 - Ovos")
    print("6 - Agua")
    print("7 - Beijinho")
    print("8 - Brigadeiro")
    print("9 - Papel Toalha")
    print("10 - Coco Ralado")
    codProd = int(input("Informe o codigo do produto: ")) - 1

    if(codProd in codigosProdutos):
      quantidadeProduto = int(input("informe a quantidade do produto: "))
      # pedido so pode ser atendido integralmente 
      if(estoquesProduto[codProd] >= quantidadeProduto):
        estoquesProduto[codProd] = estoquesProduto[codProd] - quantidadeProduto
        print("Pedido Atendido. Obrigado e volte sempre!")
      else:
        print("Não temos estoque suficiente dessa mercadoria.")
    else: 
      print("Código Inexistente.")  

print()
print("** O Estoque restante foi **")
print(codigosProdutos)
print(estoquesProduto)