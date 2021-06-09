    #Import libs

from colorthief import ColorThief
from turtle import *
import numpy as np
import matplotlib.pyplot as plt

    #Indicar arquivo imagem na pasta do projeto

ladraoDeCor = ColorThief('screen.jpg')

    #Pegar COR PIXEL dominante

corDominante = ladraoDeCor.get_color(quality=1)
screen = Screen()
colormode(255)
screen.bgcolor(corDominante)

    #Construção da palheta de cor

cores = ladraoDeCor.get_palette(color_count=6)
palette = np.array(cores)[np.newaxis, :, :]
plt.imshow(palette)
plt.axis('off')
plt.show()
