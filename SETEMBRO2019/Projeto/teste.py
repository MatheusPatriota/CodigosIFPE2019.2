import matplotlib
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)
# Define o título do gráfico e nomeia os eixos v plt.title("Square
# Numbers", fontsize=24) w 
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Define o tamanho dos rótulos das marcações x
plt.tick_params(axis='both', labelsize=14)
plt.show()