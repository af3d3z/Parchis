from Parchis import Parchis

def test_estado_carrera_empatados():
    parchis = Parchis("Pepe", "Juan")
    parchis.fichaJ1 = 3
    parchis.fichaJ2 = 3
    res = parchis.estado_carrera()
    assert res == "Pepe y Juan van empatados."
    
def test_estado_carrera_ganaj1():
    parchis = Parchis("Pepe", "Juan")
    parchis.fichaJ1 = 4
    parchis.fichaJ2 = 3
    res = parchis.estado_carrera()
    assert res == "Va ganando Pepe."
    
def test_estado_carrera_ganaj2():
    parchis = Parchis("Pepe", "Juan")
    parchis.fichaJ1 = 2
    parchis.fichaJ2 = 3
    res = parchis.estado_carrera()
    assert res == "Va ganando Juan."