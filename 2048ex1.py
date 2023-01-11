import numpy as np
import random


# Exercice 01 :  Initialisation \ creation  de la grille de jeu  (4*4):

def init_grid():
    grid = np.zeros((4, 4), dtype=int)  # initilalisation d'ne grille 4*4 par des "0"
    grid[np.random.randint(4), np.random.randint(4)] = 2  # Generer aleatoirement 2 sur la matrice
    grid[np.random.randint(4), np.random.randint(4)] = 2  # Generer aleatoirement 2 sur la matrice
    return grid
