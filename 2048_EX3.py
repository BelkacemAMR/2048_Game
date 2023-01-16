
# exercice 3:
# la fonction qui fait rouler la ligne vers la gauche et la retourne:
def rollin_row(row):
# initialisation de la ligne
    new_row = [0,0,0,0]
    j = 0
    previous = None
    for i in range(len(row)):
    # création de la boucle for:
    # si l'element est différent de zero
        if row[i] != 0:
            # si l'element precedent est vide
            if previous == None:
                # retourner i vers l'element precedent
                previous = row[i]
            else:
                # si l'element precedent n'est pas vide
                if previous == row[i]:
                    # fait l'adition de j et i
                    new_row[j] = 2 * row[i]
                    j += 1
                    previous = None
                else:
                    new_row[j] = previous
                    j += 1
                    previous = row[i]
        if previous != None:
                new_row[j] = previous
