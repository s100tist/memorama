
class Casilla:
    es_visible:         bool
    esta_seleccionada:  bool 
    simbolo:            str

    #Constructor
    def __init__(self, simbolo_inicial: str = "", es_visible_inicial: bool = False) -> None:
        self.es_visible = es_visible_inicial
        self.simbolo = simbolo_inicial
    
    
    def set_simbolo(self,simbolo:str) -> None:
        self.simbolo = simbolo

    def get_simbolo(self) -> str:
        return self.simbolo

