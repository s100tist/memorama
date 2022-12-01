import randomizacion
from Casilla import Casilla

class Tablero:
    puntuacion:             int
    casilla_seleccionada1:   dict
    casilla_seleccionada2:   dict
    cursor:                  dict
    casillas:               list[list[any]]

    #Constructor
    def __init__(self): 
        self.puntuacion = 0
        self.casilla_seleccionada = {'x':-1,'y':-1}
        self.casilla_seleccionada2 = {'x':-1,'y':-1}
        self.casillas=[list(range(6)) for _ in range(6)]
        self.cursor = {'x':0,'y':0}



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
                elif (i == self.cursor['x'] and j == self.cursor['y']):
                    print('⏹️',end="")
                else:
                    print('🛑',end="")
            print("")

    def cambiar_estado_casilla(self,coordenadas: dict)->None:
        self.casillas[coordenadas['x']][coordenadas['y']].cambiar_visibilidad()
    

    def rastrear_teclas(self,tecla:str)->None:
        coordenada_x = self.cursor['x']
        coordenada_y = self.cursor['y']
        if (tecla == "up" and self.cursor['y'] < 5):
            self.cursor['y'] += 1
        elif (tecla == "down" and self.cursor['y']>0):
            self.cursor['y'] -= 1
        elif (tecla == "right" and self.cursor['x'] < 5):
            self.cursor['x'] += 1
        elif (tecla == "left" and self.cursor['x'] > 0):
            self.cursor['x'] -= 1
        elif tecla == "enter":
            self.casillas[coordenada_x][coordenada_y].cambiar_visibilidad()


        


