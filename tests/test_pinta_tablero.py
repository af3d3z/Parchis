from Parchis import Parchis

"""
Antiguo, ya no funciona
def test_pinta_tablero_linea_numeros():
    Parchis.TAM_TABLERO = 5
    tablero = Parchis.pinta_tablero()
    assert tablero == "\tI\t1\t2\t3\t4\tF"
"""
 
def test_pinta_tablero_lineas_jugadores():
    parchis = Parchis("Pepe", "Maria")
    parchis.fichaJ1 = 2
    parchis.fichaJ2 = 2
    Parchis.TAM_TABLERO = 5
    tablero = parchis.pinta_tablero()
    tablero_test = "\tI\t1\t2\t3\t4\tF\n"
    tablero_test += "Pepe\tI\t\to\t\t\tF\n"
    tablero_test += "Maria\tI\t\to\t\t\tF\n"
    assert tablero == tablero_test
    
    
def test_pinta_tablero_1():
    parchis = Parchis("Marco", "Elena")
    parchis.fichaJ1 = 3
    parchis.fichaJ2 = 3
    Parchis.TAM_TABLERO = 5
    tablero = parchis.pinta_tablero()
    tablero_test = "\tI\t1\t2\t3\t4\tF\n"
    tablero_test += "Marco\tI\t\t\to\t\tF\n"
    tablero_test += "Elena\tI\t\t\to\t\tF\n"
    assert tablero == tablero_test
    
def test_pinta_tablero_win():
    parchis = Parchis("Grogu", "Mando")
    parchis.fichaJ1 = 5
    parchis.fichaJ2 = 5
    Parchis.TAM_TABLERO = 5
    tablero = parchis.pinta_tablero()
    tablero_test = "\tI\t1\t2\t3\t4\tF\n"
    tablero_test += "Grogu\tI\t\t\t\t\tF\n"
    tablero_test += "Mando\tI\t\t\t\t\tF\n"
    assert tablero == tablero_test
    
def test_pinta_tablero_inicio():
    parchis = Parchis("Britney", "Gaga")
    parchis.fichaJ1 = 1
    parchis.fichaJ2 = 1
    Parchis.TAM_TABLERO = 5
    tablero = parchis.pinta_tablero()
    tablero_test = "\tI\t1\t2\t3\t4\tF\n"
    tablero_test += "Britney\tI\to\t\t\t\tF\n"
    tablero_test += "Gaga\tI\to\t\t\t\tF\n"
    assert tablero == tablero_test