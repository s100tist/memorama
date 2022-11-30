import keyboard as kb
from time import sleep
from Tablero import Tablero


tablero = Tablero()
tablero.crearTablero(6)

def detectarTecla(): 
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

    return tecla_str


while(True):
    sleep(0.1)
    print(detectarTecla())