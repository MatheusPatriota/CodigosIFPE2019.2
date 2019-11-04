# Aluno: Matheus da Silva Coimbra Patriota
# Matricula: 20192EWBJ0027
# Curso: Engenharia de Software

# funcao que checa se e palindromo ou nao
def isPalindromo(palavra):
    # variaveis auxiliares
    palavraInvertida = ""
    palavra = palavra.lower()
    # percorre a string de tras para frente
    for i in range(len(palavra)-1,-1,-1):
        palavraInvertida += palavra[i]
    # checagem de igualdade
    if palavra == palavraInvertida:
        return True
    else:
        return False

# testes e impressoes
print(isPalindromo("arara"))
print(isPalindromo("ovo"))
print(isPalindromo("Matheus"))
print(isPalindromo("araRinha"))
