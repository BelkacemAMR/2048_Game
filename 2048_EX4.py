# Exercice 4:
# Script de la fonction rollin qui gére les deplacements sur la grille :

def rollin(grid, direction):
    if direction == 'l':
        return np.array([rollin_row(row) for row in grid])
    elif direction == 'r':
        return np.array([list(reversed(rollin_row(list(reversed(row))))) for row in grid])
    elif direction == 'u':
        return np.transpose(rollin(np.transpose(grid), 'l'))
    elif direction == 'd':
        return np.transpose(rollin(np.transpose(grid), 'r'))