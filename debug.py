from Casilla import Casilla
from Tablero import Tablero

casilla = Casilla()
print(casilla.get_es_visible())
print(casilla.get_simbolo())
print(casilla.get_esta_seleccionada())

# casilla.set_es_visible(True)
# casilla.set_simbolo('😎')
# casilla.set_es_visible(True)

print(casilla.get_es_visible())
print(casilla.get_simbolo())
print(casilla.get_esta_seleccionada())


tablero = Tablero()
tablero.crearTablero(6)
print(tablero.get_casillas)

tablero.imprimirCasillas()
print("")

tablero.cambiarEstadoCasilla({'x':2,'y':2})
print("")

tablero.imprimirCasillas()
print("")

tablero.cambiarEstadoCasilla({'x':2,'y':2})
print("")

tablero.imprimirCasillas()

tablero.cambiarEstadoCasilla({'x':2,'y':2})
print("")

tablero.imprimirCasillas()
tablero.cambiarEstadoCasilla({'x':2,'y':2})
print("")

tablero.imprimirCasillas()
