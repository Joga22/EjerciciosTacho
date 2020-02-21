# JGGP_reves.py

from tkinter import *
import Tablas as re


class TabMul():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Tablas_Multilicar")
        num = IntVar()
        self.numLabel = Label(self.ventana, text="Ingrese la tabla de multiplicar que desea")
        self.numEntry = Entry(self.ventana, textvariable=num)
        self.checkButton = Button(self.ventana, text="Checar", command=lambda: re.tablas(num.get()))

        self.numLabel.grid(column=0,row=0)
        self.numEntry.grid(column=1,row=0)
        self.checkButton.grid(column=0,row=1)
        
rand = TabMul()
