# problema_8.py

from tkinter import *
import crea_random as cr


class ProblemaOcho():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Compara_random")
        numero = IntVar()
        
        self.numeroLabel = Label(self.ventana, text="Ingrese un numero")
        self.numeroEntry = Entry(self.ventana, textvariable=numero)
        self.numeroButton = Button(self.ventana, text="Checar", command=lambda: cr.cuenta(numero.get()))

        self.numeroLabel.grid(column=0,row=0)
        self.numeroEntry.grid(column=0,row=1)
        self.numeroButton.grid(column=1,row=0)
        
rand = ProblemaOcho()
