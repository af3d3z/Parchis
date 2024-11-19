from Parchis import Parchis

def test_es_ganador_j1():
    parchis = Parchis("Pepe", "Manolo")
    parchis.fichaJ1 = 20
    parchis.fichaJ2 = 6
    res = parchis.es_ganador()
    assert res == parchis.nombre1
    
def test_es_ganador_j2():
    parchis = Parchis("Pepe", "Manolo")
    parchis.fichaJ1 = 2
    parchis.fichaJ2 = 20
    res = parchis.es_ganador()
    assert res == parchis.nombre2
    
def test_es_ganador_nadie():
    parchis = Parchis("Pepe", "Manolo")
    parchis.fichaJ1 = 8
    parchis.fichaJ2 = 10
    res = parchis.es_ganador()
    assert res == ""