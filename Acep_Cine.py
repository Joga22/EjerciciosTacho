# Acep_Cine.py
"""
comparara 2 numeors random
"""
import random

def cuenta(ed, cl):
    if cl == 1:
        print("Puedes pasar")
    else:
        if cl == 2:
            if ed < 15:  
                print("No puedes pasar")
            else:
                print("puedes pasar")

        if cl == 3:
            if ed < 18:  
                print("No puedes pasar")
            else:
                print("puedes pasar")
