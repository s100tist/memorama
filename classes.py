class Tablero:
    puntuacion: int

    #Constructor
    def __init__(self, puntuacion_inicial: int): 
        self.puntuacion = 0

    #Getters and setters
    # def __getattribute__(self, __name: str) -> Any:
    #     pass

    def get_puntuacion(self) -> int:
        return self.puntuacion
    
    # Metodo
    #TODO: Randomizar los simbolos
    # def crearTablero(self, tamanio_tablero: int):
        


class Casilla:
    es_visible: bool
    simbolo: str

    #Constructor
    def __init__(self, simbolo_inicial: str = "", es_visible_inicial: bool = False):
        self.es_visible = es_visible_inicial
        self.simbolo = simbolo_inicial
