def addition(a, b):
    """
    Ajoute deux nombres.

    :param a: Le premier nombre.
    :param b: Le second nombre.
    :return: La somme de a et b.
    """
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro non permise")
    return a / b