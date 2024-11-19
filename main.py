from Parchis import Parchis

def main():
    nomJ1 = input("Introduce el nombre del primer jugador:")
    nomJ2 = nomJ1
    while nomJ1 == nomJ2:
        nomJ2 = input("Introduce el nombre del segundo jugador: ")
    
    parchis = Parchis(nomJ1, nomJ2)
    
    ganador = False
    turno = 1
    
    while not ganador:
        
        
        
        if parchis.es_ganador() != "":
            ganador = True
            print(parchis.es_ganador())
    
    
if __name__ == '__main__':
    main()
    
    