# JGGP_aceptadp_cine.py

from tkinter import *
import Login as lo


class ALogin():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Aceptado_Cine")
        usu = StringVar()
        pas = StringVar()
        self.usuLabel = Label(self.ventana, text="Usuario")
        self.pasLabel = Label(self.ventana, text="Contraseña")
        self.usuEntry = Entry(self.ventana, textvariable=usu)
        self.pasEntry = Entry(self.ventana, textvariable=pas)
        self.checkButton = Button(self.ventana, text="LogIn", command=lambda: lo.logi(usu.get(), pas.get()))

        self.usuLabel.grid(column=0,row=0)
        self.pasLabel.grid(column=0,row=1)
        self.usuEntry.grid(column=1,row=0)
        self.pasEntry.grid(column=1,row=1)
        self.checkButton.grid(column=0,row=3)
        
rand = ALogin()
