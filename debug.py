import pprint
import clases
import randomizacion
tablero=clases.Tablero
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(clases.Tablero.crearTablero(tablero,6))
casilla = clases.Casilla()
casilla.set_simbolo('s')
print(casilla.get_simbolo())