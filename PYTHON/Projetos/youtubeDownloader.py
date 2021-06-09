import time
import sys
import random
from pytube import YouTube

    #pedindo o link ao usuario
yEntrada = YouTube(input('Qual o URL da musica: https://'))

    #detalhes do video
print(f'Title: {yEntrada.title} ')

    #Pegando a maior resolucao possivel
ySaida = yEntrada.streams.get_audio_only()

    #Comecando Download
print('Downloading...')
ySaida.download()
print('Download Concluido!')