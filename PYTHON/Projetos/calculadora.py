from tkinter import *
import parser
from math import factorial

calculadora = Tk()
calculadora.title('GF - CALCULADORA')
calculadora.mainloop()

    #criando campo de entrada
display = Entry(calculadora)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)

    #criando os botoes numerais da calculadora
Button(calculadora, text='1', command=lambda: getVariables(1)).grid(row=2, column=0, sticky=N+S+E+W)
Button(calculadora, text='2', command=lambda: getVariables(2)).grid(row=2, column=1, sticky=N+S+E+W)
Button(calculadora, text='3', command=lambda: getVariables(3)).grid(row=2, column=2, sticky=N+S+E+W)

Button(calculadora, text='4', command=lambda: getVariables(4)).grid(row=3, column=0, sticky=N+S+E+W)
Button(calculadora, text='5', command=lambda: getVariables(5)).grid(row=3, column=1, sticky=N+S+E+W)
Button(calculadora, text='6', command=lambda: getVariables(6)).grid(row=3, column=2, sticky=N+S+E+W)

Button(calculadora, text='7', command=lambda: getVariables(7)).grid(row=4, column=0, sticky=N+S+E+W)
Button(calculadora, text='8', command=lambda: getVariables(8)).grid(row=4, column=1, sticky=N+S+E+W)
Button(calculadora, text='9', command=lambda: getVariables(9)).grid(row=4, column=2, sticky=N+S+E+W)

    #criando outros botoes
Button(calculadora, text='AC', command=lambda: clearAll()).grid(row=5, column=0, sticky=N+S+E+W)
Button(calculadora, text='0', command=lambda: getVariables(0)).grid(row=5, column=1, sticky=N+S+E+W)
Button(calculadora, text='.', command=lambda: getVariables('.')).grid(row=5, column=2, sticky=N+S+E+W)

Button(calculadora, text='+', command=lambda: getOperation('+')).grid(row=2, column=3, sticky=N+S+E+W)
Button(calculadora, text='-', command=lambda: getOperation('-')).grid(row=3, column=3, sticky=N+S+E+W)
Button(calculadora, text='*', command=lambda: getOperation('*')).grid(row=4, column=3, sticky=N+S+E+W)
Button(calculadora, text='/', command=lambda: getOperation('/')).grid(row=5, column=3, sticky=N+S+E+W)

    #criando operações especificas
Button(calculadora, text='pi', command=lambda: getOperation('*3.14')).grid(row=2, column=4, sticky=N+S+E+W)
Button(calculadora, text='%', command=lambda: getOperation('%')).grid(row=3, column=4, sticky=N+S+E+W)
Button(calculadora, text='(', command=lambda: getOperation('(')).grid(row=4, column=4, sticky=N+S+E+W)
Button(calculadora, text='exp', command=lambda: getOperation('**')).grid(row=5, column=4, sticky=N+S+E+W)

Button(calculadora, text='<-', command=lambda: undo()).grid(row=2, column=5, sticky=N+S+E+W)
Button(calculadora, text='x!', command=lambda: fact()).grid(row=3, column=5, sticky=N+S+E+W)
Button(calculadora, text=')', command=lambda: getOperation(')')).grid(row=4, column=5, sticky=N+S+E+W)
Button(calculadora, text='^2', command=lambda: getOperation('**2')).grid(row=5, column=5, sticky=N+S+E+W)

Button(calculadora, text='=', command=lambda: calculate()).grid(columnspan=6, sticky=N+S+E+W)

    #mapeando os digitos
i = 0  # 'i' serve para manter o cursor dentro do campo

#receber os digitos e parametros exibindo eles no campo.
def getVariables(num):
    global i
    display.insert(i, num)
    i += 1

def getOperation(operador):
    global i
    display.insert(i, operador)
    i += len(operador)

def clearAll():
    display.delete(0, END)

def undo():
    entireString = display.get()
    if len(entireString):
        newString = entireString[:-1]
        clearAll()
        display.insert(0, newString)
    else:
        clearAll()
        display.insert(0, 'ERRO')

def calculate():
    entireString = display.get()
    try:
        a = parser.expr(entireString).compile()
        result = eval(a)
        clearAll()
        display.insert(0, result)
    except Exception:
        clearAll()
        display.insert(0, 'ERRO')

def fact():
    entireString = display.get()
    try:
        result = factorial(int(entireString))
        clearAll()
        display.insert(0, result)
    except Exception:
        clearAll()
        display.insert(0, 'ERRO')

