import matplotlib.pyplot as plt
import numpy as np

class Maze:
    def __init__(self, rows : int, cols : int):
        """ Initialisation des parametres importants du labyrinthe : Rows et Cols """
        self.rows = rows
        self.cols = cols
        self.maze = np.zeros((rows, cols), dtype=int)

        # Initialisation des murs exterieurs du labyrinthe avec l'entrée et la sortie
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and ((i,j) != (0,1) and (i,j) != (rows-1, cols-2)):
                    self.maze[i, j] = 1


    def pyplot(self):
        """ Affichage du labyrinthe """
        fig, ax = plt.subplots()
        ax.imshow(self.maze, cmap='binary')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()

    def main_droite(self):
        """ Algorithme de la main droite """
        
        pass



laby = Maze(40, 40)
laby.pyplot()
