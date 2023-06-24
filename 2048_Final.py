# Projet formation Data Analyst
# La Manu , Janvier 2023
# Jeu 2048 , Python avec Pygame
# AMROUN Belkacem.
# Zaoioui Meriam
# Import des Packages :

import pygame

from random import choice
from pygame.locals import*
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


#Initialisation:

pygame.init()
pygame.font.init()

#Définition de la fenétre de jeu:
WIDTH, HEIGHT = 750, 750
CAPTION = '2048 By Belkacem'

TOP, LEFT = 200, 200
BLOCK_WIDTH, BLOCK_HEIGHT = 100, 100
GAP = 10

###########################################################################
MAIN_MENU_FONT = pygame.font.SysFont('Helvitica', 75)

TITLE_FONT = pygame.font.SysFont('Baskerville', 75)
BLOCK_FONT = pygame.font.SysFont('Baskerville', 25)
STATS_FONT = pygame.font.SysFont('Baskerville', 40)
GAME_OVER_FONT = pygame.font.SysFont('Baskerville', 45)

# Définition des couleurs :

BLACK = '#000000'
WHITE = '#ffffff'
BLUE =  '#0000ff'
RED =   '#ff0000'

BG_COLOR = '#bbada0'
0
COLOR_MAP = {
    0:     ('#CCC0B4', None),
    2:     ('#eee4da', '#776e65'),
    4:     ('#ede0c8', '#776e65'),
    8:     ('#f2b179', '#f9f6f2'),
    16:    ('#f59563', '#f9f6f2'),
    32:    ('#f67c5f', '#f9f6f2'),
    64:    ('#f65e3b', '#f9f6f2'),
    128:   ('#edcf72', '#f9f6f2'),
    256:   ('#edcc61', '#f9f6f2'),
    512:   ('#edc850', '#f9f6f2'),
    1024:  ('#edc53f', '#f9f6f2'),
    2048:  ('#edc22e', '#f9f6f2'),
    4096:  ('#eee4da', '#776e65'),
    8192:  ('#edc22e', '#f9f6f2'),
    16384: ('#f2b179', '#776e65'),
    32768: ('#f59563', '#776e65'),
    65536: ('#f67c5f', '#f9f6f2')
}

#############################################################################################
############################################################################################
############################################################################################

ecran = pygame.display.set_mode((700, 500))
image = pygame.image.load("LaManu.png").convert_alpha()

continuer = True

while continuer:
    ecran.blit(image, (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()



######################################################Statistiques############################################################################""

# # Initialisation des compteurs à 0
#
statistic = 0
up_count = 0
down_count = 0
left_count = 0
right_count = 0


#####################################################################################################################################"

class App_2048:
    '''2048 App Class'''
    def __init__(self, end: int = None) -> None:

        self.end = end
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        image = pygame.image.load("LaManu.png").convert()
        pygame.display.set_caption(CAPTION)




    def init_variables(self):
        self.running = True
        self.score = 0
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.add_block()

    def exit(self) -> None:

        pygame.quit()
        quit()

    def rot90(self, matrix: list[list]) -> list[list]:

        return [list(reversed(row)) for row in zip(*matrix)]

    def rot180(self, matrix: list[list]) -> list[list]:

        return self.rot90(self.rot90(matrix))

    def rot270(self, matrix: list[list]) -> list[list]:

        return self.rot180(self.rot90(matrix))

    def push_right(self) -> None:

        for col in range(len(self.grid[0]) - 2, -1, -1):
            for row in self.grid:
                if row[col + 1] == 0:
                    row[col], row[col + 1] = 0, row[col]
                elif row[col + 1] == row[col]:
                    self.score += row[col] * 2
                    print("Votre score est de :",self.score)
                    row[col], row[col + 1] = 0, row[col] * 2

    def right(self) -> None:


        self.push_right()
        self.update()

    def left(self) -> None:

        self.grid = self.rot180(self.grid)
        self.push_right()
        self.grid = self.rot180(self.grid)
        self.update()

    def up(self) -> None:

        self.grid = self.rot90(self.grid)
        self.right()
        self.grid = self.rot270(self.grid)
        if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_UP:
                        up_count += 1
        self.update()

    def down(self) -> None:

        self.grid = self.rot270(self.grid)
        self.push_right()
        self.grid = self.rot90(self.grid)
        self.update()
#####################################################################################################################################################






    def game_state(self) -> str:


        if self.end:
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    if self.grid[row][col] == self.end:
                        return 'WIN'

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 0:
                    return 'BLOCK AVAILABLE'

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row]) - 1):
                if self.grid[row][col] == self.grid[row][col + 1]:
                    return 'CAN MERGE'

        for row in range(len(self.grid) - 1):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == self.grid[row + 1][col]:
                    return 'CAN MERGE'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()






        return 'LOSE'

    def add_block(self) -> None:

        free_blocks = [(y, x) for y, row in enumerate(self.grid) for x, num in enumerate(row) if num == 0]
        y, x = choice(free_blocks)
        self.grid[y][x] = 2

    def update(self) -> None:

        state = self.game_state()
        if state == 'WIN':
            self.game_over(True)
        elif state == 'LOSE':
            self.game_over(False)
        elif state == 'BLOCK AVAILABLE':
            self.add_block()

    def game_over(self, win: bool) -> None:
        '''Ends the game'''
        self.draw_win()
        if win:
            label = GAME_OVER_FONT.render(f'You won! You scored {self.score} points.', 1, BLUE)

        else:
            label = GAME_OVER_FONT.render(f'Perdu! Votre score est de : {self.score} points.', 1, RED)

        self.win.blit(label, (WIDTH//2 - label.get_width()//2,
            HEIGHT//2 - label.get_height()//2))
        pygame.display.update()
        pygame.time.delay(3000)
        self.running = False

    def draw_win(self) -> None:

        self.win.fill(BLACK)
        self.draw_grid()
        self.draw_stats()

    def draw_grid(self) -> None:

        pygame.draw.rect(self.win, BG_COLOR,
            (LEFT - GAP, TOP - GAP, len(self.grid[0]) * (BLOCK_WIDTH + GAP) + GAP,
            len(self.grid) * (BLOCK_HEIGHT + GAP) + GAP))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                x = LEFT + (col * (BLOCK_WIDTH + GAP))
                y = TOP + (row * (BLOCK_HEIGHT + GAP))
                value = self.grid[row][col]
                bg_color, font_color = COLOR_MAP[value]
                color_rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
                pygame.draw.rect(self.win, bg_color, color_rect)

                if value != 0:
                    label = BLOCK_FONT.render(str(value), 1, font_color)
                    font_rect = label.get_rect()
                    font_rect.center = color_rect.center
                    self.win.blit(label, font_rect)

    def draw_stats(self) -> None:

        label = TITLE_FONT.render(f'        ----- 2048 -----', 1, '#228B22')
        self.win.blit(label, (150, 5))

        label = STATS_FONT.render(f'Score: {self.score}', 1, '#FFFF00')

        self.win.blit(label, (400, 125))

    def main(self) :
        up_count = 0
        down_count = 0
        left_count = 0
        right_count = 0
        up = 0
        down = 0
        left = 0
        right = 0
        '''Main function which runs the game'''
        self.init_variables()
        while self.running:
            self.draw_win()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                    ##############################################################
                if event.type == KEYDOWN:
                    if event.key in [K_a, K_LEFT]:
                        self.left()
                        left_count += 1
                        print("Left:", left_count)
                        left = left_count

                    ###########################################################################
                    if event.key in [K_d, K_RIGHT]:
                        self.right()
                        right_count += 1
                        print("Right:", right_count)
                        right = right_count

                    ####################################################
                    if event.key in [K_w, K_UP]:
                        self.up()
                        up_count += 1
                        print("Up:", up_count)
                        up = up_count

                    ###################################################
                    if event.key in [K_s, K_DOWN]:
                        self.down()
                        down_count += 1
                        print("Down:", down_count)
                        down = down_count



        #############################################################

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        data = [up,
                down,
                left,
                right]

        Bouton = "up", "down", "left", "right"



        def func(pct, allvals):
            absolute = int(np.round(pct / 100. * np.sum(allvals)))
            return "{:.1f}%\n({:d} push)".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))

        ax.legend(wedges, Bouton,
                  title="Bouton",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title("% de push sur les boutons directionelles lors d'une session de jeu 2048")

        plt.show()

        #########################################################################################################################################################
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                  bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1) / 2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(data[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                        horizontalalignment=horizontalalignment, **kw)

        ax.set_title("% de push sur les boutons directionelles lors d'une session de jeu 2048")

        plt.show()

        ######################################################################################################################################
        fig, ax = plt.subplots()

        Directions = ['Up', 'Down', 'Left', 'Right']

        bar_labels = ['Up', 'Down', 'Left', 'Right']
        bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']

        ax.bar(Directions, data, label=bar_labels, color=bar_colors)

        ax.set_ylabel('Nbre de push')
        ax.set_title('Boutons ')
        ax.legend(title='Nbre de Push sur les touches directionelles')

        plt.show()

        ###########################################################################################################################"

        data = {'Up': up, 'Down': down, 'Left': left, 'Right': right}
        names = list(data.keys())
        values = list(data.values())

        fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
        axs[0].bar(names, values)
        axs[1].scatter(names, values)
        axs[2].plot(names, values)
        fig.suptitle("Nbre de pushs lors d'une cession de jeu de 2048")

        ###############################################################################
        # This works on both axes:
        data1 = [up, down, left, right]

        activity = ["Up", "Down", "Left", "Right"]

        fig, ax = plt.subplots()
        ax.plot(activity, data1, label="Joueur1")
        # ax.plot(activity, data, label="Joeurs2")
        ax.legend(title="Nbre de pushs lors d'une cession de jeu de 2048")

        plt.show()



        ############################################################

        self.main_menu()
        return down_count, up_count,right_count,left_count


######################################################################################################################################################
    ##################################################################################################################""""
    def main_menu(self) -> None:
        '''Runs a main menu'''
        self.win.fill(BLACK)


        pygame.display.update()


        label = MAIN_MENU_FONT.render("Bonjour !  ", 1, WHITE)


        #label1.caption = "Bonjour!" & vbNewLine & "Appuyez sur une touche pour jouer!"



        # Position du message d'acceuil sur l'écran :

        self.win.blit(label, (WIDTH//2 - label.get_width()//2,
            HEIGHT//2 - label.get_height()//2))
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
                if event.type in [KEYDOWN, MOUSEBUTTONDOWN]:
                    running = False
        self.main()





###################################################################################################################################################################
###################################################################################################################################################################
###################################################################################################################################################################

#########################################################################################################################################"

if __name__ == '__main__':
    app = App_2048()
    app.main_menu()
