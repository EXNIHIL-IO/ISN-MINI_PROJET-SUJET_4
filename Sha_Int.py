from math import *
from Verification import *


def Sha_Int():
    shadok = str(input('Nombre Shadok :'))
    K = int(input('Base de Sortie :'))
    if K <= 10 and K != 0 and K != 1:  # Test pour savoir si la base est prise en charge ou non
        d = 0
        shadok = shadok.lower()  # Passe la chaine en minuscule (Python est sensible à la casse)
        shadok = shadok.replace(' ', '')  # Retire les espaces
        B = shadok.replace('ga', '0')
        B = B.replace('bu', '1')
        B = B.replace('zo', '2')
        B = B.replace('meu', '3')  # Transforme "bu" "ga" "zo" 'meu" en "0" "1" "2" "3"
        v = verif_shadok(B)  # Vérifie si le nombre shadok entré est correct
        if v == 0:
            a = int(B)
            while a != 0:
                b = int(log(a, K))  # b prend la valeur de log(a)/log(K)
                a -= K ** b  # a est décrémenté K^b
                d += 4 ** b  # d est incrémenté de 4^b
            result = [shadok, B, d, K]  # shadok = Nbr langage Shadok ; B = Nbr Base 4 ; d = Nombre converti en base 'K'
            return result  # Retourne la liste contenant les résultats
        else:
            result = 2
            return result  # Retourne le code d'erreur "2"
    else:
        result = 1
        return result  # Retourne le code d'erreur "1"
