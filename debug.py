import pprint
import Tablero

tablero = Tablero()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(Tablero.Tablero.crearTablero(tablero,6))

print(type(Tablero))