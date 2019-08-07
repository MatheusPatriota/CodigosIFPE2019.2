# Assunto : Conhecimento gerais

def iniciarQuiz():
    pontuacao = 0
    
    print ("BEM VINDO - VAMOS INICIAR O QUIZZ:")
    nome  = input("DIGITE SEU NOME: ")
    print ("Vamos lah " +  nome.upper())

    p1 = input(" qual a capital do Brasil? \n A)RIO DE JANEIRO \n B)BRASIL \n C)CARIOCA \n D)BRASILIA \n")
    if p1 == 'A':
        print ("Voce errou!")
    elif p1 == 'B':
        print ("Voce errou!")
    elif p1 == 'C':
        print ("Voce errou!")
    elif p1 == 'D':
        print ("Certa Resposta!")
        pontuacao = pontuacao + 1
    else:
        print ("Resposta nao cadastrada")
    
    p2 = input(" qual a cidade conhecida como cidade maravilhosa? \n A)APOCALIPSE \n B)RECIFE \n C)RIO DE JANERIO \n D)NENHUMA \n")
    if p2 == 'A':
        print ("Voce errou!")
    elif p2 == 'B':
        print ("Voce errou!")
    elif p2 == 'C':
        print ("Certa Resposta!")
        pontuacao = pontuacao + 1
    elif p2 == 'D':
        print ("Voce errou!")
    else:
        print ("Resposta nao cadastrada")

    p3 = input(" qual a raiz quadrada de 9? \n A)2 \n B)3 \n C)5 \n D)8 \n")
    if p3 == 'A':
        print ("Voce errou!")
    elif p3 == 'B':
        print ("Certa Resposta!")
        pontuacao = pontuacao + 1
    elif p3 == 'C':
        print ("Voce errou!")
    elif p3 == 'D':
        print ("Voce errou!")
    else:
        print ("Resposta nao cadastrada")    

    print(nome + " voce teve " + str(pontuacao) + " pontos")




    
print ("Bem vindo Ao QUIZZ FIQUE MILIONARIO SABENDO SOBRE JOGOS")
print ("deseja participar?")
opcao = input(" 1 - SIM \n 2 - NAO \n")

if opcao == '1':
    iniciarQuiz()
else:
    print("Ate logo")



