from sudoku_classes import *
from generate_sudoku import *
import random

#concept


#consider each of the subcubes in some random but fixed order (rerandomised each iteration)

#for each cube, randomly take a point, and after it is chosen remove it's x,y,z coordinate from
#relevant sets containing partitioned x y and z variables

#proceed iteratively through remaining subcubes, but only consider points with x, y, z coordinates
#still in relevant sets

#once all subcubes have had an element selected, restore sets of x y and z values
#rerandomise order of subcubes, and start over, now not taking any point selected from previous iteration

#loop until n values selected




#Not quite latin hypercube sampling - can only ever manage an approximation because of the subsquare 
#property of Sudoku boards meaning that our variables are not all mutually independent.

#should still guarantee as even a distribution as can be hoped for ('even' defined by how many spaces are
#'adjacent' to each other in Sudoku terms, not by physical distance measures)

def determine_subsquare_order(available_indices):
    """randomly determine order of subsquares from which we will remove elements"""
    order = list(range(27))
    random.shuffle(order)
    
    for subcube in order:
        yield available_indices[subcube]
        

def generate_available_indices():
    """generate dictionary of possible coordinate values for each subcube"""
    remaining_indices = {}
    for i in range(3):
        for j in range(3):
            for k in range(3):
                z_coords = {3*i, 3*i+1, 3*i+2}
                y_coords = {3*j, 3*j+1, 3*j+2}
                x_coords = {3*k, 3*k+1, 3*k+2}
                remaining_indices[9*i + 3*j + k] = [x_coords, y_coords, z_coords]
                
    return remaining_indices


def main():
    sudoku_ls = generate_unshuffled_3d_board()
    
    available_indices = generate_available_indices()


main()