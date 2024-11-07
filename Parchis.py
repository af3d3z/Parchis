import random

class Parchis:
    TAM_TABLERO = 20
    dado1 = 0
    dado2 = 0

    def tira_dados():
        Parchis.dado1 = random.randint(1, 6)
        Parchis.dado2 = random.randint(1, 6)
        
    def pinta_tablero(self):
        tablero = ""
        for i in range(0, Parchis.TAM_TABLERO+1):
            if i == 0:
                tablero += "\tI"
            elif i == Parchis.TAM_TABLERO:
                tablero += "\tF\n"
            else:
                tablero += f"\t{i}"
                
        for i in range(0, 2):
            for j in range(0, Parchis.TAM_TABLERO+1):
                if j == 0:
                    tablero += (self.nombre1 if i == 0 else self.nombre2) + "\tI"
                elif j == Parchis.TAM_TABLERO:
                    tablero += "\tF\n"
                else:
                    if (i == 0 and j == self.fichaJ1) or (i == 1 and j == self.fichaJ2):
                        tablero += "\to"
                    else:
                        tablero += "\t"
            
        return tablero
    
    
    def avanza_posiciones(self, jugador):
        Parchis.tira_dados()
                

    def __init__(self, nombre1, nombre2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nombre1 = nombre1
        self.nombre2 = nombre2