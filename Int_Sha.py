from math import *
from Verification import *


def Int_Sha():
    S = int(input('Nombre à convertir:'))
    K = int(input('Base d\'entrée :'))
    if K <= 10 and K != 0 and K !=1:  # Test pour savoir si la base est prise en charge ou non
        v = verif_base(S, K)  # Vérifie si le nombre entré en base "K" est correct
        if v == 0:
            d = 0
            a = S  # Fait une copie du nombre à convertir
            while a != 0:
                b = int(log(a, 4))  # b prend la valeur de log(a)/log(4)
                a -= 4 ** b  # a est décrémenté 4^b
                d += K ** b  # d est incrémenté de K^b
            shadok = str(d)  # Copie le nombre converti en base 4
            shadok = shadok.replace('0', 'ga')
            shadok = shadok.replace('1', 'bu')
            shadok = shadok.replace('2', 'zo')
            shadok = shadok.replace('3', 'meu')  # Traduit la copie du nombre converti  en base 4 en langage Shadok
            result = [S, K, d, shadok]  # B = Base 4 ; shadok = Nbr langage Shadok ; d = Nombre converti en base 'K'
            return result  # Retourne la liste contenant les résultats
        else:
            result = 2
            return result  # Retourne le code d'erreur "2"
    else:
        result = 1
        return  result  # Retourne le code d'erreur "1"
