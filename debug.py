import pprint
import Tablero
tablero=Tablero.Tablero
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(Tablero.Tablero.crearTablero(tablero,6))
casilla = Tablero.Casilla()
casilla.set_simbolo('s')
print(casilla.get_simbolo())