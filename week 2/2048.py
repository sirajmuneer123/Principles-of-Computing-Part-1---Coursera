

#import poc_simpletest   # for test
import random
import poc_2048_gui

#Directions, DO NOT MODIFY
UP= 1
DOWN= 2
LEFT= 3
RIGHT= 4

#Offsets for computing tile indices in each direction.
#DO NOT MODIFY this dictionary.    
OFFSETS= {UP: (1, 0), 
          DOWN: (-1, 0), 
          LEFT: (0, 1), 
          RIGHT: (0, -1)} 

def merge(line):
     # replace with your code
    old_leng=len(line)
    remove(line)
    new_leng=len(line)
    for value in range(new_leng-1):
        if line[value]==line[value+1] and value+1<new_leng:
            line[value]=line[value]*2
            line[value+1]=0
    remove(line)
    last_leng=len(line)
    times=old_leng-last_leng
    for value in range(times):
        line.append(0)
    return line


def remove(line):
    #remove zerros
    leng=len(line)
    for value in range(leng):
        if 0 in line:
            line.remove(0)
    return line
#print merge([2,2,4,4,4,16,16,0,0,0,0])
                                             

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.row_number = grid_height
        self.col_number = grid_width
        self.grid = [[0 for _ in range(self.col_number)] for _ in range(self.row_number)]     
        #print self.grid
      
        # store the lists of initial tiles
        self.init_tiles = dict()
        self.init_tiles[UP]    = zip([ 0 for i in range(grid_width)], [i for i in range(grid_width)])
        self.init_tiles[DOWN]  = zip([grid_height - 1 for i in range(grid_width)], [i for i in range(grid_width)])
        self.init_tiles[LEFT]  = zip([i for i in range(grid_height)], [0 for i in range(grid_height)])
        self.init_tiles[RIGHT] = zip([i for i in range(grid_height)], [grid_width - 1 for i in range(grid_height)])

        # 9 2s and 1 4
        self.empty_list = list()
        self.new_tile_list = [ 2 for i in range(9)]
        self.new_tile_list.append(4)
        #print self.new_tile_list



    def traverse_empty_tiles(self):
        """ raverse grid and get empty tile position"""
        self.empty_list = list()    # reset list

        for row in range(self.row_number):
            for col in range(self.col_number):
                if self.grid[row][col] == 0:
                    self.empty_list.append( (row,col) )


    def print_init_tiles(self):
        """ 
        print init_tiles, for test purpose
        """
        for key in self.init_tiles.items():
            print (key)

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [[0 for _ in range(self.col_number)] for _ in range(self.row_number)]     
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str = '' 
        for row in range(self.row_number):
            grid_str += ''.join(str(self.grid[row]))
            grid_str += '\n'
        return grid_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.row_number
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.col_number 

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == DOWN:
            print " Down" 
        # list_len used to create list
        if direction == UP or direction == DOWN:
            list_len = self.row_number
        else:
            list_len = self.col_number

        tiles = self.init_tiles[direction]
        offset = OFFSETS[direction]
        print "Offset:" + str(offset) + '\n'

        # get the tile value, call merge function and then set it back
        for tile in tiles:
            print "current tile:" + str(tile) 
            line = list()

            row, col = tile[0], tile[1] 

            for _ in  range(list_len):                  # _ for used variable
                line.append( self.get_tile(row, col) )
                row, col = row + offset[0], col + offset[1]
            print line
            merge(line)
            print line
            row, col = tile[0], tile[1] 
            for it_row in range(list_len):
                print row,col
                self.set_tile(row, col, line[it_row])
                row, col = row + offset[0], col + offset[1]
        
        print self.__str__()
        self.new_tile()
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # question 1: how to randomly select an empty square
            # loop through matrix, record empty tile pos into a list
            # get the list size and generate a random number mod list size, 
            # got the random empty tile pos

        self.traverse_empty_tiles()
        #print self.grid
        #print self.empty_list
        list_size = len(self.empty_list)

        rand_pos = random.randint(0, list_size - 1)
        rand_new = random.randint(0,9)

        # question 2: how to generate 2 in 90% and 4 in 10%
            # have a list with 9 2 and 1 4, generate a ramdom index access
        row, col = self.empty_list[rand_pos][0], self.empty_list[rand_pos][1]
        self.set_tile(row, col, self.new_tile_list[rand_new])
    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        if row < 0 or row >= self.row_number or col < 0 or col >= self.col_number:
            print "Out of grid bound"
            return -1
        self.grid[row][col] = value
    
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        if row < 0 or row >= self.row_number or col < 0 or col >= self.col_number:
            print "Out of grid bound"
            return -1
        return self.grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(3, 3))

