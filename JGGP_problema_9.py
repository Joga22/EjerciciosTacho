# problema_9.py

from tkinter import *
import contador_cadena as cc

class ProblemaNueve():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Contador_Cadena")
        cadena = StringVar()
        self.cadenaLabel = Label(self.ventana, text="Ingrese una palabra")
        self.cadenaEntry = Entry(self.ventana, textvariable=cadena)
        self.cadenaButton = Button(self.ventana, text="Checar", command=lambda: cc.cuenta(cadena.get()))

        self.cadenaLabel.grid(column=0,row=0)
        self.cadenaEntry.grid(column=0,row=1)
        self.cadenaButton.grid(column=1,row=0)
        
conta = ProblemaNueve()
