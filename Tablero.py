import randomizacion
from Casilla import Casilla

class Tablero:
    puntuacion:             int
    casilla_seleccionada1:   dict
    casilla_seleccionada2:   dict
    casillas:               list[list[any]]

    #Constructor
    def __init__(self): 
        self.puntuacion = 0
        self.casilla_seleccionada = {'x':0,'y':0}
        self.casilla_seleccionada2 = {'x':0,'y':0}
        self.casillas=[list(range(6)) for _ in range(6)]

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
                if (i == self.casilla_seleccionada['x'] and j == self.casilla_seleccionada['y']):
                    print('⏹️',end="")
                else:
                    print('🛑',end="")
            print("")

    def cambiarEstadoCasilla(self,coordenadas: dict)->None:
        self.casillas[coordenadas['x']][coordenadas['y']].cambiar_visibilidad()
    

    def rastrearTeclas(tecla:str)->None:
        print(tecla)

        


