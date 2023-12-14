import matplotlib.pyplot as plt
import numpy as np

class Maze:
    def __init__(self, rows : int, cols : int):
        """ Initialisation des parametres importants du labyrinthe : Rows et Cols """
        self.rows = rows
        self.cols = cols
        self.maze = np.zeros((rows, cols), dtype=int)
    

    def pyplot(self):
        fig, ax = plt.subplots()
        ax.imshow(self.maze, cmap='binary')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()



laby = Maze(10, 10)
laby.pyplot()

        
