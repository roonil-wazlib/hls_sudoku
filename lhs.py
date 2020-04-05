from sudoku_classes import *
from generate_sudoku import *
import random
import copy

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



def order_generator(available_indices):
    """randomly determine order of subsquares from which we will remove elements"""
    order = list(range(27))
    random.shuffle(order)
    
    for subcube in order:
        yield available_indices[subcube]
        


def get_subcube_indices():
    """
    Generate dictionary of possible coordinate values for each subcube.
    Used as a reference point for determining the subset of coordinates we can
    choose from at each stage.
    """
    remaining_indices = {}
    for i in range(3):
        for j in range(3):
            for k in range(3):
                z_coords = {3*i, 3*i+1, 3*i+2}
                y_coords = {3*j, 3*j+1, 3*j+2}
                x_coords = {3*k, 3*k+1, 3*k+2}
                remaining_indices[9*i + 3*j + k] = [x_coords, y_coords, z_coords]
                
    return remaining_indices



def get_available_coordinates():
    """
    Generate available coordinate values for overall cube, in form
       coordinates = [{x_coords}, {y_coords}, {z_coords}]
       
    Part used for latin hypercube sampling aspect of algorithm.
    """
    
    coordinates = []
    for _ in range(3):
        coordinates.append(set(range(9)))
        
    return coordinates


def get_blank_game():
    """build a blank game to be populated overtime"""
    game = []
    for _ in range(9):
        plane = []
        for _ in range(9):
            plane.append([0] * 9)
        game.append(plane)
        
    return game


def build_game(num_blank):
    """generate a game of Sudoku with num_blank blank squares, evenly distributed about the board."""
    
    #since all boards isomorphic to a uniquely solvable game should also be uniquely solvable (??),
    #we need only check the ordered case
    sudoku_ls = generate_unshuffled_3d_board()
    
    #generate initial coordinate values, and subcube reference
    subcube_indices = get_subcube_indices()
    available_coordinates = get_available_coordinates()
    
    #generate blank game that we will slowly populate
    #since we know the optimal solution has well over half the squares blank, it is faster to populate than to unpopulate
    #evenly distributing populated squares is the same as evenly distributing unpopulated squares
    game = get_blank_game()
    
    num_selected = 0
    #keeps track of the number of times we've looped
    count = 0
    
    while num_selected < 729 - num_blank:
        
        coordinates_this_loop = copy.deepcopy(available_coordinates)
        #loop through subcubes
        for item in order_generator(subcube_indices):
            x = list(item[0].union(coordinates_this_loop[0]))[0]
            y = list(item[1].union(coordinates_this_loop[1]))[0]
            z = list(item[2].union(coordinates_this_loop[2]))[0]
            
            print(item[0].union(coordinates_this_loop[0]))
            print(x, y, z)
            print(item)
            coordinates_this_loop[0].remove(x)
            coordinates_this_loop[1].remove(y)
            coordinates_this_loop[2].remove(z)
            
            game[x][y][z] = ""
            
            num_selected += 1
            
    
    return game
    


def main():
    print(build_game(500))


main()