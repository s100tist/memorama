import randomizacion

class Tablero:
    puntuacion:             int
    casilla_seleccionada:   dict

    #Constructor
    def __init__(self): 
        self.puntuacion = 0

    #Getters and setters
    # def __getattribute__(self, __name: str) -> Any:
    #     pass

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

        


class Casilla:
    es_visible:         bool
    esta_seleccionada:  bool 
    simbolo:            str

    #Constructor
    def __init__(self, simbolo_inicial: str = "", es_visible_inicial: bool = False):
        self.es_visible = es_visible_inicial
        self.simbolo = simbolo_inicial
    
    
    def set_simbolo(self,simbolo:str):
        self.simbolo = simbolo
    def get_simbolo(self):
        return self.simbolo

