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

    # Algorithme du labyrinthe parfait 
  def generate_perfect_maze(self):
        """ Génère la structure d'un labyrinthe parfait en utilisant l'algorithme de DFS """
        stack = [(1, 1)]  # Pile pour stocker les cellules à visiter
        visited = set([(1, 1)])  # Ensemble pour stocker les cellules visitées

        while stack:
            current = stack[-1]
            i, j = current

            # Trouver les voisins non visités
            neighbors = [(i + 2, j), (i - 2, j), (i, j + 2), (i, j - 2)]
            unvisited_neighbors = [(ni, nj) for ni, nj in neighbors if 0 < ni < self.rows - 1 and 0 < nj < self.cols - 1 and (ni, nj) not in visited]

            if unvisited_neighbors:
                # Choisir un voisin aléatoire
                next_cell = random.choice(unvisited_neighbors)

                # Supprimer le mur entre les cellules actuelle et suivante
                wall = ((i + next_cell[0]) // 2, (j + next_cell[1]) // 2)
                self.maze[wall[0], wall[1]] = 0

                # Marquer la cellule suivante comme visitée et l'ajouter à la pile
                visited.add(next_cell)
                stack.append(next_cell)
            else:
                # Retirer la cellule actuelle de la pile s'il n'y a plus de voisins non visités
                stack.pop()
        



    def main_droite(self):
        """ Algorithme de la main droite """
        
        pass



laby = Maze(40, 40)
laby.pyplot()
