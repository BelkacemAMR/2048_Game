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

# Exercice 03 :
