from Parchis import Parchis

def test_avanza_posiciones_j1_basico():
    juego = Parchis("Manolo", "Pepe")
    juego.fichaJ1 = 5
    Parchis.dado1 = 3
    Parchis.dado2 = 4
    juego.avanza_posiciones(1)
    assert juego.fichaJ1 == 12

def test_avanza_posiciones_j2_basico():
    juego = Parchis("Manolo", "Pepe")
    juego.fichaJ2 = 3
    Parchis.dado1 = 2
    Parchis.dado2 = 5
    juego.avanza_posiciones(2)
    assert juego.fichaJ2 == 10

def test_avanza_posiciones_j1_supera_tablero():
    juego = Parchis("Manolo", "Pepe")
    juego.fichaJ1 = Parchis.TAM_TABLERO - 1
    Parchis.dado1 = 5
    Parchis.dado2 = 5
    juego.avanza_posiciones(1)
    assert juego.fichaJ1 == 11

def test_avanza_posiciones_j2_supera_tablero():
    juego = Parchis("Manolo", "Pepe")
    juego.fichaJ2 = Parchis.TAM_TABLERO - 3
    Parchis.dado1 = 4
    Parchis.dado2 = 5
    juego.avanza_posiciones(2)
    assert juego.fichaJ2 == 14

def test_avanza_posiciones_j1_inicio():
    juego = Parchis("Manolo", "Pepe")
    juego.fichaJ1 = 0
    Parchis.dado1 = 3
    Parchis.dado2 = 6
    juego.avanza_posiciones(1)
    assert juego.fichaJ1 == 9

def test_avanza_posiciones_j1_dados_0():
    juego = Parchis("Manolo", "Pepe")
    juego.fichaJ1 = 5
    Parchis.dado1 = 0
    Parchis.dado2 = 0
    juego.avanza_posiciones(1)
    assert juego.fichaJ1 == 5
