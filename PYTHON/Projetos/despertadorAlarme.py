        # Importando as libs necessarias para a forma do despertador:
from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        datahoraAtual = datetime.datetime.now()
        horarioAgora = datahoraAtual.strftime('%H:%M:%S')
        dataAgora = datahoraAtual.strftime('%d/%m/%Y')
        print(f'a DATA DEFINIDA é: {dataAgora}')
        print(horarioAgora)
        if horarioAgora == set_alarm_timer:
            print('HORA de ACORDAR!')
            winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f'{hora.get()}:{min.get()}:{seg.get()}'
    alarm(set_alarm_timer)

        # CRIANDO INTERFACE:
relogio = Tk()

relogio.title('GF DESPERTADORES')
relogio.geometry('400x200')
formatoRelogio = Label(relogio, text='DIGITE o HORARIO no FORMATO de 24hrs', fg='red', bg='black',
                       font='Arial').place(x=60, y=120)
addHora = Label(relogio, text='Hour  Min   Sec', font=60).place(x=200)
setDespertador = Label(relogio, text='que HORAS voce QUER ACORDAR?', fg='blue', relief='solid',
                       font=('Arial', 7, 'bold')).place(x=0, y=29)

        # Variaveis necessarias para definir a inicialização do despertador:
hora = StringVar()
min = StringVar()
seg = StringVar()

        # Horario requerido para definir o despertador:
horaHorario = Entry(relogio, textvariable=hora, bg='pink', width=15).place(x=200, y=30)
minHorario = Entry(relogio, textvariable=min, bg='pink', width=15).place(x=240, y=30)
segHorario = Entry(relogio, textvariable=seg, bg='pink', width=15).place(x=280, y=30)

        # Fazer o Usuário entrar com o horario:
submit = Button(relogio, text='DEFINIR ALARME', fg='red', width=20, command=actual_time).place(x=110, y=70)

        # Execução da Janela
relogio.mainloop()
