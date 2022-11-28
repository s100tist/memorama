import random

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
    def randomizarEmojis():
        emojis = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😇', '😉', '😊', '🙂', '🙃', '👻', '💀', '🥵', '👽', '🤖']
        listaRes = list()
        lista = list(range(0,36))
        random.shuffle(lista)

        for i in lista:
            if i>17:
                listaRes.append(emojis[35-i])
            else:
                listaRes.append(emojis[i])
        print(listaRes)

    # def crearTablero(self, tamanio_tablero: int):
        


class Casilla:
    es_visible: bool
    simbolo: str

    #Constructor
    def __init__(self, simbolo_inicial: str = "", es_visible_inicial: bool = False):
        self.es_visible = es_visible_inicial
        self.simbolo = simbolo_inicial
