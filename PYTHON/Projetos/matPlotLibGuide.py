from matplotlib import pyplot as plt
plt.style.use("ggplot")

# VALORES EIXO _X
eixoX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# VALORES EIXO _Y
linhaA = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
linhaB = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
linhaC = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

#CRIANDO GRAFICO e ESTILIZANDO as LINHAS
plt.plot(eixoX, linhaA, color='k', linestyle="--", marker="o", label="Linha A")
plt.plot(eixoX, linhaB, color="b", marker="o", linewidth=3, label="Linha B")
plt.plot(eixoX, linhaC, color="y", marker="o", linewidth=3, label="Linha C")

#PLOT SETUP
plt.xlabel("EIXO X label")
plt.ylabel("EIXO Y label")
plt.title("MATPLOTLIB DEMONSTRAÇÃO")
plt.grid(True)
plt.legend()
plt.show()