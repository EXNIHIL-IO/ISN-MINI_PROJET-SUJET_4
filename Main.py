R = 1
while R == 1:
    Q = str(input("""Que voulez vous faire ?
              - Convertir du système Shadok vers un entier (1)
              - Convertir d\'un entier vers le système Shadok (2)
              - Changer un entier de base (3)
    : """))  # Choix du mode à utiliser
    Q = Q.replace(' ', '')
    if str(Q) == '1':  # Mode 1
        from Sha_Int import *  # Importe la fonction Sha_Int définie dans Sha_Int.py

        resultat = Sha_Int()  # Resutat prend la valeur 1; 2 ou prend la forme d'une liste
        if resultat == 1:  # Si resultat vaut 1 (Code d'erreur)
            print('Cette base n\'est pas prise en charge')
            R = int(input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: '))
        elif resultat == 2:  # Si resultat vaut 2 (Code d'erreur)
            print('Ce nombre shadok n\'est pas correct')
            R = int(input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: '))
        else:  # Sinon (Si resultat est une liste) afficher la liste retournée par la fonction
            print(resultat[0], '=', resultat[1], 'en base 4 et', resultat[2], 'en base', resultat[3])
            R = int(input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: '))
    elif str(Q) == '2':  # Mode 2
        from Int_Sha import *  # Importe la fonction Int_Sha définie dans Int_Int.py

        resultat = Int_Sha()  # Resutat prend la valeur 1; 2 ou prend la forme d'une liste
        if resultat == 1:  # Si resultat vaut 1 (Code d'erreur)
            print('Cette base n\'est pas prise en charge')
            R = input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: ')
        elif resultat == 2:  # Si resultat vaut 2 (Code d'erreur)
            print('Le nombre que vous avez rentré est incorrect.')
            R = input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: ')
        else:  # Sinon (Si resultat est une liste) afficher la liste retournée par la fonction
            print(resultat[0], 'en base', resultat[1], '=', resultat[2], 'en base 4 et', resultat[3],
                  'en système Shadok')
            R = input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: ')
    elif str(Q) == '3':  # Mode 3
        from Base_Converter import *  # Importe la fonction Base_Converter définie dans Base_Converter.py

        resultat = Base_Converter()  # Resutat prend la valeur 1; 2 ou prend la forme d'une liste
        if resultat == 1:  # Si resultat vaut 1 (Code d'erreur)
            print('Cette base n\'est pas prise en charge')
            R = input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: ')
        elif resultat == 2:  # Si resultat vaut 2 (Code d'erreur)
            print('Le nombre que vous avez rentré est incorrect.')
            R = input('Appuyez sur ENTREE pour fermer le programme : ')
        else:  # Sinon (Si resultat est une liste) afficher la liste retournée par la fonction
            print(resultat[0], 'en base', resultat[1], '=', resultat[2], 'en base', resultat[3])
            R = input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: ')
    else:
        print('Ce mode n\'existe pas !')
        R = input('Entrez "0" pour fermer le programme ou "1" pour effectuer une autre conversion: ')
exit()
