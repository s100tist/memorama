import randomizacion
from Casilla import Casilla

class Tablero:
    puntuacion:             int
    casilla_seleccionada:   dict
    casillas:               list[list[any]]

    #Constructor
    def __init__(self): 
        self.puntuacion = 0
        self.casilla_seleccionada = {'x':0,'y':0}
        self.casillas=[list(range(6)) for _ in range(6)]

    #Getters and setters
    # def __getattribute__(self, __name: str) -> Any:
    #     pass

    def get_puntuacion(self) -> int:
        return self.puntuacion
    
    def get_casillas(self)-> list:
        return self.casillas

    # Metodos


    def crearTablero(self, tamanio_tablero: int)->None:
        conta = 0
        emojis = randomizacion.randomizarEmojis()
        for i in range(tamanio_tablero):
            for j in range(tamanio_tablero):
                casilla = Casilla()
                casilla.set_simbolo(emojis[conta])
                self.casillas[i][j] = casilla
                conta += 1

    def imprimirCasillas(self)->None:
        for i in range(len(self.casillas)):
            for j in range(len(self.casillas[0])):
                if self.casillas[i][j].get_es_visible() == True:
                    print (self.casillas[i][j].get_simbolo(),end="")
                else:
                    print('🛑',end="")
            print("")

    def cambiarEstadoCasilla(self,coordenadas: dict)->None:{
        self.casillas[coordenadas['x']][coordenadas['y']].set_es_visible()
    }

        


