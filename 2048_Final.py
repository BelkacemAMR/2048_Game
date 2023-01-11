import numpy as np
import random


# Exercice 01 :  Initialisation de la grille avec

def init_grid():
    grid = np.zeros((4, 4), dtype=int)  # initilalisation d'ne grille 4*4 par des "0"
    grid[np.random.randint(4), np.random.randint(4)] = 2  # Generer aleatoirement 2 sur la matrice
    grid[np.random.randint(4), np.random.randint(4)] = 2  # Generer aleatoirement 2 sur la matrice
    return grid



# Exercice 02:  Ajout de Nouveaux elements dans la grille.

def add_new(grid):
    ajout_valeur = random.choice([2, 2, 2, 2, 4])  # 5 elements 100% 4 elements 80% + 1 element 20%
    position = random.choice(list(
        zip(*np.where(grid == 0))))  # Ajout de la valeur precedente dans la grille ou la valeur de la cellule est de 0
    grid[position] = ajout_valeur
    return grid



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