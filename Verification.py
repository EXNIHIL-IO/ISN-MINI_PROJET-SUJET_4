def verif_base(n, b):  # n = nombre à tester ; b = base du nombre à tester
    t = 10 - b  # t = Nombre de test que le programme doit effectuer
    d = int(0)
    chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # Liste contenant tout les chiffres
    resultat = 0
    del chiffres[0:b]  # Supprime les chiffres qui sont normalement utilisés pour écrire un nombre en base 'b'
    while d != t:  # Tant qu'il n'a pas éffectué tous les tests le programme continue
        if chiffres[d] in str(n):  # Si un chiffre qui ne devrait pas être là est detecté
            resultat = 1  # resultat prend la valeur 1 (code d'erreur)
        d += 1  # Ajoute 1 au rang du test avant de passer au suivant
    return resultat  # Retourne la valeur "resultat" : 0 = Nombre correct ; 1 = Nombre incorrect


def verif_shadok(shadok):  # shadok = nombre shadok converti en base 4 à tester
    resultat = 0 # initialisation de la variable resultat à 0
    for element in shadok:  # Pour chaque élement (caractère) de la chaîne shadok les action suivantes sont répétées
        if element == "0" or element == "1" or element == "2" or element == "3": # on teste si l'élément est un chiffre possible en base 4
            resultat = resultat  # Si oui alors la valeur de la variable resultat ne change pas
        else: #si non alors :
            resultat = 1 # resultat est défini à 1 (code d'erreur), la ligne 18 garantie un changement irréversible
    return resultat # Retourne la valeur "resultat" : 0 = Nombre correct ; 1 = Nombre incorrect
