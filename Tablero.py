import randomizacion

class Tablero:
    puntuacion:             int
    casilla_seleccionada:   dict
    casillas:               list[list[any]]

    #Constructor
    def __init__(self): 
        self.puntuacion = 0

    def get_puntuacion(self) -> int:
        return self.puntuacion
    
    # Metodos


    def crearTablero(self, tamanio_tablero: int):
        #creamos una matriz de 'tamaño' x 'tamaño'
        tab2 = self.__init__
        tab2 = [list(range(tamanio_tablero)) for _ in range(tamanio_tablero)]
        emojis = randomizacion.randomizarEmojis()
        conta = 0
        for i in range(tamanio_tablero):
            for j in range(tamanio_tablero):
                tab2 [i][j] = emojis[conta]
                conta = conta + 1  

        return tab2

        


