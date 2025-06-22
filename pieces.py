from points import Point as P
import utils
import pygame
import math

class Tetromino:
    '''
    A class representing a Tetromino piece in the Tetris game. The Tetromino is defined by its name, vertices,
    color, and current position on the board.

    Attributes:
        name (str):        The name of the Tetromino piece (e.g., 't', 'o', 'l', etc.).
        verts (list):      A list of Point objects representing the vertices of the Tetromino in the current position.
        color (tuple):     The RGB color of the Tetromino.
        orientation (int): The current orientation of the Tetromino (0, 1, 2, or 3).
        squares (list):    A list of Point objects representing the positions of the top left corners of the
                           squares that form the Tetromino.
    '''
    
    def __init__(self, name, verts, color, orientation = 0, dx = 0, dy = 0):
        '''
        Initializes a new instance of the Tetromino class.

        Args:
            name (str): The name of the Tetromino piece (e.g., 't', 'o', 'l', etc.).
            verts (list): A list of Point objects representing the vertices of the Tetromino.
            color (tuple): The RGB color of the Tetromino.
            orientation (int):  Keep track of orientation of the piece, defaults to 0
            dx (int, optional): The x-offset to apply to the vertices. Default is 0.
            dy (int, optional): The y-offset to apply to the vertices. Default is 0.
        '''

        self.name        = name
        self.verts       = [P(v.x + dx, v.y + dy) for v in verts]
        self.color       = color
        self.orientation = orientation
        self.squares     = utils.get_square_positions(self.name, self.verts, self.orientation)

    def __str__(self):
        '''
        Returns a string representation of the Tetromino, showing its vertices.

        Returns:
            str: A string representation of the Tetromino vertices.
        '''

        return 'verts '+str(self.verts)+'\ncolor: '+str(self.color) +' orientation: '+str(self.orientation) 
            
    def move(self, dx, dy):
        '''
        Moves the Tetromino by a specified amount in the x and y directions.

        Args:
            dx (int): The distance to move in the x direction.
            dy (int): The distance to move in the y direction.

        '''

        #updates tetromino position by adding dx and dy
        #shifts vertexes by specified amount
        self.verts = [P(v.x + dx, v.y + dy) for v in self.verts]

        #recalculate positions of the squares of each tetromino after moving
        #updates squares based on calculations
        self.squares = utils.get_square_positions(self.name, self.verts, self.orientation)

        pass
    
    def get_pivot(self):
        '''
        Returns the pivot point of the Tetromino, which is the point around which the piece will rotate.

        Returns:
            Point: The pivot point of the Tetromino.
        
        '''

        #if no vertices then it returns a default point of origin
        if not self.verts:
            return P(0,0)
        
        sum_x = 0
        for v in self.verts:
            sum_x += v.x

        sum_y = 0
        for v in self.verts:
            sum_y += v.y

        #calculates average of x and y coordinates
        avg_x = sum_x/len(self.verts)
        avg_y = sum_y/len(self.verts)

        return P(avg_x, avg_y)  

        pass
    
 
    


        

    def rotate(self):
        '''
        Rotates the Tetromino 90 degrees clockwise around its pivot point.
        The vertices are recalculated, and the orientation is updated.

        Variables:
        pivot (P): The pivot point around which the rotation is done
        rotated_vertices (list of P): list of vertexes after rotating them 90 degrees clockwise.
        self.verts (list of P): updated positions of vertices of the Tetromino after being rotated
        self.squares (list of P): updated positions of the squares that make up the Tetromino
        self.orientation (int): The current orientation of the Tetromino
    

        '''
        
        #get pivot point
        pivot = self.get_pivot()
        
        # rotates vertices around th epivot point
        self.verts = [v.rotate(pivot) for v in self.verts]
        
        # round x and y coordinates down to align them to grid
        self.verts = [P(math.floor(v.x), math.floor(v.y)) for v in self.verts]
        
        # updates orientation to between 0 and 3
        self.orientation = (self.orientation + 1) % 4
        
        # update position of self.squares using the new rotated vertices and orientation
        self.squares = utils.get_square_positions(self.name, self.verts, self.orientation)

        pass


    def copy(self):
        '''
        Get a new copy of the object

        Variables:
        new_name: str 
        new_verts: list of P
        new_color: str of tuple
        new_orientation: int


        '''
        new_name = self.name
        new_verts = self.verts
        new_color = self.color
        new_orientation = self.orientation

        #creates a new Tetromino object with the same attributes as the current one
        new_tetronimo = Tetromino(new_name, new_verts, new_color, new_orientation)

        return new_tetronimo
        pass
        
        
    def draw(self, screen, pix_size = 30):
        '''
        Draws the Tetromino on the provided Pygame screen surface.

        Args:
            screen (pygame.Surface): The Pygame surface on which to draw the Tetromino.
            pix_size (int, optional): The size of each pixel in the game grid. Default is 30.
        '''
        
        get_points = lambda : [(v.x*pix_size, v.y*pix_size) for v in self.verts]
        pygame.draw.polygon(screen, self.color, get_points())


if __name__=='__main__':


    pass

