# Login.py
"""
Login
"""
import random

def logi(usu, pas):
    if usu == "utng":
        if pas == "mexico":
            print("bienvenido")
        else:
            print("contraseña incorrecta")
    else:
        print("usuario incorrecto")
        
