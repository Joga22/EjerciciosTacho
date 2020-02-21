# JGGP_reves.py

from tkinter import *
import ParImpar as re


class NumImPar():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Numero_Par_Impar")
        num = IntVar()
        self.numLabel = Label(self.ventana, text="Ingrese un numero")
        self.numEntry = Entry(self.ventana, textvariable=num)
        self.checkButton = Button(self.ventana, text="Checar", command=lambda: re.conv(num.get()))

        self.numLabel.grid(column=0,row=0)
        self.numEntry.grid(column=1,row=0)
        self.checkButton.grid(column=0,row=1)
        
rand = NumImPar()
