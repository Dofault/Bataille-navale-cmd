from queue import Empty
import random
from string import ascii_letters

print("\033c") #ignorer
#variable-----------------------------------

def creer_plateau(grille) :
    
    lgne=str('abcdefghij')
    ligne=[" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    grille.append(ligne)
    for j in range(10) :
        ligne=[]
        
        ligne.append(lgne[j])
        for i in range(10) :
            ligne.append(0)
        grille.append(ligne)

def afficher(grille) :
    tmp = "    "
    for i in range(1, len(grille)) :
        tmp= tmp + " | " + str(grille[0][i])
    print(tmp + "|")
    print(" ____|___|___|___|___|___|___|___|___|___|___|")
    
    for i in range(1, len(grille)) :
        tmp = " | " + grille[i][0]
        for j in range(1, len(grille)) :
            if grille[i][j] == 0 :
                tmp = tmp + " | " + str(" ")
            elif grille[i][j] == 1 :
                    
                tmp = tmp + " | " + str("1")
            elif grille[i][j] == 2 :
                tmp = tmp + " | " + "X"
            
            elif grille[i][j] == 3 :
                tmp=tmp + " | " + "-"
        print(tmp + " |")
        
        print(" |---|-----------------------------------------")

def remplir_bateau(grille, taille, placement, lettre, col) :

    # lettre = lettre de la colonne
    ligne= ord(lettre) - 96

    if grille[ligne][col] == 0 :

        if placement== "h" :
            #doit pas depasser la matrice
            if col + taille > 11 :
                print("Erreur, la taille du bateau dépasse le plateau !")
                return False

            # Verification si le bateau touche aucun autre bateau
            for j in range(taille) :
                for x in range(-1, 2) :
                    for y in range(-1, 2) :
                        # print("comparaison ligne : " + str(ligne+x) + " et col : " + str(col+y+j))
                        if ligne + x <= 10 and col + y + j <= 10 and ligne + x > 0 and col + y + j > 0 :
                            if grille[ligne + x][col + y+j] == 1 :
                                print("Erreur, un bateau ne peut pas en toucher un autre !")
                                return False
            
            # si disponible on l'ajoute
            ligneModif = grille[ligne]
            for i in range(taille) :
                ligneModif[i+col]= 1
            grille[ligne] = ligneModif
        else:
            if placement== "v" :
                # verticale
                if ligne + taille > 11 :
                    print("Erreur, la taille du bateau dépasse le plateau !")
                    return False

                # Verification si le bateau touche aucun autre bateau
                for j in range(taille) :

                    for x in range(-1, 2) :
                        for y in range(-1, 2) :
                            
                            # x : offset de la ligne
                            # y : offset de la colonne

                            # si la position testé est dans le tableau
                            if ligne + x <= 10 and col + y <= 10 and ligne + x > 0 and col + y > 0 :
                                #print("ligne testé : " + str(ligne+x) + ", col : " + str(col + y))
                                if grille[ligne + x][col + y] == 1 :
                                    print("Erreur, un bateau ne peut pas en toucher un autre !")
                                    return False
                
                
                # si disponible on l'ajoute
                for i in range(taille) :
                    ligneModif = grille[i+ligne]
                    ligneModif[col]= 1
                    grille[i+ligne] = ligneModif
        return True
    else :
        print("Cette coordonnée est déjà associé à un bateau !")
        return False

def attaquer(grille, lettre, col) :

    ligne = ord(lettre) - 96

    print(ligne, col)   
    val =grille[ligne][col] 
    # Si l'attaque est dans l'eau
    if val == 0:
        print("Missile tombé à l'eau !")
        ligneModif=[]
        ligneModif= grille[ligne]
        ligneModif[col] = 3
        grille[ligne] = ligneModif
        return True

    # Si bateau touché
    elif val == 1 :
        print("Bateau touché !")
        print(grille[ligne][col])
        ligneModif=[]
        ligneModif= grille[ligne]
        ligneModif[col] = 2
        grille[ligne] = ligneModif
        return True

    # Si bateau touché déjà essayé, renvoie False pour que l'utilisateur réessaye
    elif val == 2:
        print("Le bateau à cette coordonnée a déjà été touché !")
        
        print(grille[ligne][col])
        return False

    elif val == 3:
        print("Cette coordonnée déjà été essayé aupparavant")
        return False

def fin(grille) :
    partie = False
    for i in range(1, len(grille)) :
        for j in range(1, len(grille)) :
            if grille[i][j]== 1 :
                partie= True
    return partie


print("Création du plateau...")
matrice=[]
creer_plateau(matrice)

afficher(matrice)
situation="Y"

while situation == "Y" :

    print("Saisissez les coordonnées du bateau entre A01 et J10(qui sera allongé vers le bas ou à droite): ")
    coord= str(input())
    # extraction des valeurs à comparer
    if coord != "" :
        asci= ord(coord[0].lower()) - 96

    # condition pour eviter les crash
    col=0
    if len(coord) == 3 and coord[1].isnumeric() and coord[2].isnumeric() :
        col=int(coord[1]) * 10 + int(coord[2])
    else :
        col = 0

    # Doit contenir 3 caractères, commencer par une lettre et se terminer par 3 chiffres entre A01 et J10
    while coord == "" or len(coord) != 3 or coord[0].isnumeric() or not (coord[1].isnumeric() or coord[2].isnumeric()) or asci < 1 or asci > 10 or (col> 10 or col < 1):
        print("Veuillez saisir une coordonné valide pour le bateau entre A01 et J10 : ")
        coord= str(input())
        

        # extraction des valeurs à comparer
        if coord != "" :
            asci= ord(coord[0].lower()) - 96
        # condition pour eviter les crash
        if len(coord) == 3 and coord[1].isnumeric() and coord[2].isnumeric() :
            
            col=int(coord[1]) * 10 + int(coord[2])

    # VERTICAL OU HORIZONTALE
    print("Le bateau verticalement (V) ou horizontalement(H) :")
    disposition = str(input())
    disposition = disposition.lower()

    while not (disposition == "v" or disposition == "h") :
        print("Erreur de disposition, H pour horizontale, V pour verticale :")
        disposition=str(input())
        disposition = disposition.lower()

    ajout = False
    tail="t"
    print("Taille du tableau :")
    tail = input()
    while ajout == False :
        while not tail.isnumeric() :
            print("erreur rentrez une taille valide : ")
            tail=input()

        taille = int(tail) 
        
        lettre = str(coord[0].lower())

        ajout = remplir_bateau(matrice, taille, disposition.lower(), lettre, col)
        if ajout == False :
            print("Nouvelle taille, STOP pour arreter l'ajout")
            tail=input()
            if not tail.isnumeric() and tail == "STOP":
                break

    afficher(matrice)
    if not ajout :
        print("(Bateau non ajouté)")

    print("Voulez-vous ajouter un nouveau bateau ? Y / N")
    situation = str(input())
    while(situation != "Y" and situation != "N") :
        situation = str(input())


print("Fin du placement des bateaux, début de la partie ! ")


partie = True

while partie == True :

    print("Saisissez une coordonnée pour le missile :")
    missile=str(input())


    if not missile == "" :
        asci= ord(missile[0].lower()) - 96
    else :
        asci = 0

    
    if len(missile) == 3 and missile[1].isnumeric() and missile[2].isnumeric() :
        col=int(missile[1]) * 10 + int(missile[2])
    # Condition coordonnée du missile
    while missile == "" or len(missile) != 3 or missile[0].isnumeric() or not (missile[1].isnumeric() or missile[2].isnumeric()) or asci < 1 or asci > 10 or (col> 10 or col < 1):
        print("Veuillez saisir une coordonnée valide pour le missile entre A01 et J10 : ")
        missile=str(input())
        
        # extraction des valeurs à comparer
        if not missile == "" :
            asci= ord(missile[0].lower()) - 96

        # condition pour eviter les crash
        if len(missile) == 3 and missile[1].isnumeric() and missile[2].isnumeric() :
            col=int(missile[1]) * 10 + int(missile[2])

    col=int(missile[1]) * 10 + int(missile[2])
    attaquer(matrice, missile[0].lower(), col)
    afficher(matrice)
    partie = fin(matrice)