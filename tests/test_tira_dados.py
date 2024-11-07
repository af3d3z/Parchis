from Parchis import Parchis


def test_tira_dados():
    Parchis.tira_dados()
    num1 = Parchis.dado1
    num2 = Parchis.dado2
    assert (0 < num1 <= 6) and (0 < num2 <= 6)