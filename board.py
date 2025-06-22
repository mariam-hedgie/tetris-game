import pygame

class Block:
    
    '''
        A class to represent an individual block in the Tetris game grid.

        Attributes:
            x (int): The x-coordinate of the block.
            y (int): The y-coordinate of the block.
            color (tuple): The RGB color of the block.
    '''
        
    def __init__(self, p, color):
        '''
        Initializes a new block.

        Args:
            p (Point): A Point object representing the block's position.
            color (tuple): The RGB color of the block.
        '''
        
        self.x     = p.x
        self.y     = p.y
        self.color = color

    def draw(self, screen, p_size):
        '''
        Draws the block on the game screen.

        Args:
            screen (pygame.Surface): The Pygame surface where the block will be drawn.
            p_size (int): The size of the block in pixels.
        '''
        
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * p_size, self.y * p_size, p_size, p_size))



class Board:
    '''
    A class to represent the Tetris game board.
    
    Attributes:
        width (int): The width of the game board (in blocks).
        height (int): The height of the game board (in blocks).
        pix_size (int): The pixel size of each block. (Used for visualization purposes)
        grid (list): A 2D list representing the grid of blocks (None for empty cells, Block for filled).
    '''

    def __init__(self, w, h, pixel_size = 30):
        '''
        Initializes the Tetris game board.

        Args:
            w (int): The width of the board in number of blocks.
            h (int): The height of the board in number of blocks.
            pixel_size (int, optional): The size of each block in pixels. Default is 30.
        '''

        self.width    = w
        self.height   = h
        self.pix_size = pixel_size
        self.grid     = [[None for _ in range(self.width)] for _ in range(self.height)]

        
    def check_collision(self, tet):
        '''
        Checks if the active Tetromino has collided with the edges of the board or other placed blocks.

        Args:
            tet (Tetromino): The Tetromino object currently falling.
        
        Returns:
            bool: True if there is a collision, False otherwise.
        '''

        for square in tet.squares: 
            #convert coordinates to integers for precise alignment with grid
            square.x, square.y = int(square.x), int(square.y)

            #check if square is out of right, left or lower bound
            if square.x < 0 or square.x >= self.width or square.y >= self.height:
                return True #return true if tetronimo is out of bounds
            
            #checks if position in grid is already full
            if self.grid[square.y][square.x] is not None:
                return True #if current tetromino overlaps with another return true
            
        return False #return false if its within the bounds and not overlapping


        pass
    
    def place_tetromino(self, tet):
        '''
        Places a Tetromino on the game board by adding its blocks to the grid.

        Args:
            tetromino (Tetromino): The Tetromino object to be placed on the board.
        '''

        for s in tet.squares:
            self.grid[s.y][s.x] = Block(s, tet.color)
                                
            


    def clear_rows(self):
        
        '''
        clears rows that are fully filled and moves the grid down. it also adds new empty rows to the top of the grid.

            Variables:
            new_grid (list of lists): copy of current_grid to make changes without modyfying the original
            n (int): index of the currrent row being checked
            row (list): current row
            block (object): a block in the grid that may or may not be filled

        '''
        # creates a copy of the grid
        new_grid = self.grid.copy()

        #iterate through each row of the grid 
        for n in range(len(self.grid)):
            row = self.grid[n]
            if all(row) == True: #check if the row is fully filled
                new_grid.pop(n) #remove the row from the grid
                for i in range(n): #moves y values down as they are incremented by 1
                    for block in new_grid[i]:
                        if block != None:
                            block.y += 1
                new_grid.insert(0, [None] * self.width) #adds an empty row at the top of the grid

        #updates the current grid to the edited one
        self.grid = new_grid


        pass       

    def draw(self, screen):
        '''
        Draws the game board and all placed blocks on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface where the game board will be drawn.
        '''

        for row in self.grid:
            for block in row:
                if block:
                    block.draw(screen, self.pix_size)
        

if __name__ == "__main__":
    pass
