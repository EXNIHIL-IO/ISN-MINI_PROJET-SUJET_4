from math import *
from Verification import *


def Base_Converter():
    a = int(input('Nombre à convertir: '))
    start = a
    base = int(input("Base d\'entrée : "))
    base2 = int(input("Base de sortie : "))
    d = 0
    if base <= 10 and base2 <= 10 and base != 0 and base2 != 0 and base != 1 and base2 != 1:  # Test pour savoir si les bases sont prises en charge ou non
        v = verif_base(a, base)  # Vérifie si le nombre entré en base "base2" est correct
        if v == 0:  # Si le nombre est correct
            while a != 0:
                b = int(log(a, base2))  # b prend la valeur de log(a)/log(base2)
                a -= base2 ** b  # a est décrémenté base2^b
                d += base ** b  # d est incrémenté de base^b
            result = [start, base, d, base2]  # start = Nbr de départ en base "base"; d = Nbr converti en base "base2"
            return result  # Retourne la liste contenant les résultats
        else:
            result = 2
            return result  # Retourne le code d'erreur "2"
    else:
        result = 1
        return result  # Retourne le code d'erreur "1"
