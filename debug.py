import keyboard as kb
from Tablero import Tablero


tablero = Tablero()
tablero.crearTablero(6)


while(1):
    kb.wait("up")
    print("o")