# crea_random.py
"""
comparara 2 numeors random
"""
import random

def cuenta(nu):
    nr = random.randrange(1, 100)
    if nu == nr:
        print("Ingresaste un numero igual, tu numero: ",nu," Sistema: ",nr)
    else:
        if nu>nr:
            print("Ingresaste un numero mayor, tu numero: ",nu," Sistema: ",nr)
        else:
            print("Ingresaste un numero menor, tu numero: ",nu," Sistema: ",nr)
