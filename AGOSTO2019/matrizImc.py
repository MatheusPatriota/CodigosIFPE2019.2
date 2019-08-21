import numpy as np     
import plotly.graph_objects as go 


# 17 linhas
# 11 colunas


def calculoIMC(a, p):
    imc = p / (a**2)
    return round(imc,2)


coluna = np.arange(1.5, 2, 0.05)
linha = np.arange(50, 135, 5)
matriz = np.empty((17, 10), dtype=float)


for i in range(17):
    for j in range(10):
        imc = calculoIMC(coluna[j], linha[i])
        matriz[i][j] = imc

fig = go.Figure()

fig.add_trace(go.Heatmap(
                   z=matriz,
                   x= coluna,
                   y=linha,
                   colorscale=[[0, "rgb(215,109,109)"],
                              [0.30, "rgb(255,205,0)"],
                              [0.31, "rgb(178,223,138)"],
                              [0.40, "rgb(51,160,44)"],
                              [0.60, "rgb(251,154,153)"],
                              [1, "rgb(227,26,28)"]],))
fig.show()


