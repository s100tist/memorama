from Casilla import Casilla

casilla = Casilla()
print(casilla.get_es_visible())
print(casilla.get_simbolo())
print(casilla.get_esta_seleccionada())

casilla.set_es_visible(True)
casilla.set_simbolo('😎')
casilla.set_es_visible(True)

print(casilla.get_es_visible())
print(casilla.get_simbolo())
print(casilla.get_esta_seleccionada())
