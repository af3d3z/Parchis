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
    
    
    def avanza_posiciones(self, num):
        if num == 1:
            self.fichaJ1 += Parchis.dado1 + Parchis.dado2
            if self.fichaJ1 > Parchis.TAM_TABLERO:
                diferencia = self.fichaJ1 - Parchis.TAM_TABLERO
                self.fichaJ1 = Parchis.TAM_TABLERO - diferencia
        elif num == 2:
            self.fichaJ2 += Parchis.dado1 + Parchis.dado2
            if self.fichaJ2 > Parchis.TAM_TABLERO:
                diferencia = self.fichaJ2 - Parchis.TAM_TABLERO
                self.fichaJ2 = Parchis.TAM_TABLERO - diferencia
                
    def estado_carrera(self):
        res = ""
        if self.fichaJ1 == self.fichaJ2:
            res = f"{self.nombre1} y {self.nombre2} van empatados."
        else:
            res = f"Va ganando {self.nombre1 if self.fichaJ1 > self.fichaJ2 else self.nombre2}."
        
        return res
    
    def es_ganador(self):
        ganador = ""
        if self.fichaJ1 == Parchis.TAM_TABLERO:
            ganador = self.nombre1
        elif self.fichaJ2 == Parchis.TAM_TABLERO:
            ganador = self.nombre2
            
        return ganador

    def __init__(self, nombre1, nombre2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nombre1 = nombre1
        self.nombre2 = nombre2