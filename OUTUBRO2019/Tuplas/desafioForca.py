# Aluno: Matheus da Silva Coimbra Patriota
# matricula: 20192EWBJ0027

import random
import os

def forca(x):
    if(x==0):
        print("------|    "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|----------")
    elif(x==1):
        print("------|    "
            "\n|    ---   "
            "\n|  | O O | "
            "\n|  |  V  | "
            "\n|    ---   "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|----------")

    elif (x == 2):
        print("------|    "
            "\n|    ---   "
            "\n|  | O O | "
            "\n|  |  V  | "
            "\n|    ---   "
            "\n|     |    "
            "\n|     |    "
            "\n|     |    "
            "\n|     |    "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|----------")
          
    elif( x == 3):
        print("------|    "
            "\n|    ---   "
            "\n|  | O O | "
            "\n|  |  V  | "
            "\n|    ---   "
            "\n|     |    "
            "\n|    /|    "
            "\n|   / |    "
            "\n|     |    "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|----------")
    elif (x == 4):
        print("------|    "
            "\n|    ---   "
            "\n|  | O O | "
            "\n|  |  V  | "
            "\n|    ---   "
            "\n|     |    "
            "\n|    /|\   "
            "\n|   / | \  "
            "\n|     |    "
            "\n|          "
            "\n|          "
            "\n|          "
            "\n|----------")
    elif(x == 5):
        print("------|    "
            "\n|    ---   "
            "\n|  | O O | "
            "\n|  |  V  | "
            "\n|    ---   "
            "\n|     |    "
            "\n|    /|\   "
            "\n|   / | \  "
            "\n|     |    "
            "\n|    /     "
            "\n|   /      "
            "\n|  /       "
            "\n|----------")
    elif(x == 6):
        print("------|    "
            "\n|    ---   "
            "\n|  | O O | "
            "\n|  |  V  | "
            "\n|    ---   "
            "\n|     |    "
            "\n|    /|\   "
            "\n|   / | \  "
            "\n|     |    "
            "\n|    / \  "
            "\n|   /   \ "
            "\n|  /     \ "
            "\n|----------")
        print("Você Perdeu!")

def exibeLista(lista):
    for i in range(len(lista)):
        print(lista[i],"",end="")

# definições de temas
# jogos
jogos = [("MARIO","ESTÁ SEMPRE ENTRANDO PELO CANO",5),("COUNTER STRIKE","FPS FAMOSO E UM DOS MAIS JOGADOS ATUALMENTE",14)]

# DEFINIR MAIS DEPOIS

erros = 0
faixa = random.choice(jogos)
palavra = faixa[0]
saida = ""

for i in range(faixa[2]):
    if palavra[i] == " ":
        saida += (" ")
    else:
        saida += ("_")

saida = list(saida)
forca(erros)

while True:
    if (erros == 6):
        break
    else:
        if("_" in saida):
            print("A dica é: {:}".format(faixa[1]))
            exibeLista(saida)
            print()
            print()
            letra = input("Informe uma letra: ")
            print()
            if(letra.upper() not in palavra):
                erros+=1
                forca(erros)

            else:
                for i in range(len(palavra)):
                    if(letra.upper() == palavra[i]):
                        saida[i] = letra.upper()    
                forca(erros)  
             
        else:
            exibeLista(saida)
            print()
            print("PARABENS, VOCÊ GANHOU!")
            break
    
    