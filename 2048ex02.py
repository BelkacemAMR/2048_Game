# Exercice 02:
# Ajout de Nouveaux elements dans la grille.
import numpy as np
import random
def add_new(grid):
    ajout_valeur = random.choice([2, 2, 2, 2, 4])  # 5 elements 100% 4 elements 80% + 1 element 20%
    position = random.choice(list(
        zip(*np.where(grid == 0))))  # Ajout de la valeur precedente dans la grille ou la valeur de la cellule est de 0
    grid[position] = ajout_valeur
    return grid
