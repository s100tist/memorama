import keyboard as kb
from time import sleep
from Tablero import Tablero
import os
import time 
 
if os.name == "posix":
   var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"


tablero = Tablero()
tablero.crearTablero(6)

def detectar_tecla(): 
    tecla_str : str = ""
    while(True):
        if kb.is_pressed("up"):   
            tecla_str = "up"
            break

        elif kb.is_pressed("down"):
            tecla_str = "down"
            break

        elif kb.is_pressed("right"):
            tecla_str = "right"
            break

        elif kb.is_pressed("left"):
            tecla_str = "left"
            break
        elif kb.is_pressed("enter"):
            tecla_str = "enter"
            break
    return tecla_str


while(True):
    tablero.imprimirCasillas()
    tablero.rastrear_teclas(detectar_tecla())
    sleep(0.15)