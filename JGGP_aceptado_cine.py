# JGGP_aceptadp_cine.py

from tkinter import *
import Acep_Cine as ac


class AceptadoCine():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Aceptado_Cine")
        edad = IntVar()
        clas = IntVar()
        self.edadLabel = Label(self.ventana, text="Ingrese su edad")
        self.clasLabel = Label(self.ventana, text="Ingrese el numero de acuerdo a la clasificacion de la pelicula: 1 = Ninos, 2 = Adolescentes 3 = Adultos")
        self.edadEntry = Entry(self.ventana, textvariable=edad)
        self.clasEntry = Entry(self.ventana, textvariable=clas)
        self.checkButton = Button(self.ventana, text="Checar", command=lambda: ac.cuenta(edad.get(), clas.get()))

        self.edadLabel.grid(column=0,row=0)
        self.clasLabel.grid(column=0,row=1)
        self.edadEntry.grid(column=1,row=0)
        self.clasEntry.grid(column=1,row=1)
        self.checkButton.grid(column=0,row=3)
        
rand = AceptadoCine()
