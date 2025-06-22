class Point:

    def __init__(self, x=0, y=0):
        '''
        sets arguments as x and y attributes and defaults values to 0

        '''
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        Returns user friendly string

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
            
        return 'x: ' + str(round(self.x,4)) + ' y: ' + str(round(self.y,4))

    def __str__(self):
        '''
        Returns user friendly string

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return 'x: ' + str(round(self.x,4)) + ' y: ' + str(round(self.y,4))

    def rotate(self, pivot = None):
        '''
        rotates the current point clockwise by 90 degrees about a given point or the origin if no point is given
        
        Parameters:
        pivot (Point, optional): The point around which to the current point is rotated. Defaults to Point(0, 0)

        Returns:
        Point: A new Point object representing the new rotated coordinates

        '''
        #if no pivot point is given set it to origin
        if pivot == None:
            pivot =  Point(0, 0)

        #translate current point so pivot becomes origin
        translated_x = self.x - pivot.x
        translated_y = self.y - pivot.y

        #rotate clockwise
        rotated_x = translated_y
        rotated_y = -translated_x

        #translate the rotated point back to the original coordinate space
        final_x = rotated_x + pivot.x
        final_y = rotated_y + pivot.y

        #returns the rotated point as a point object
        return Point(final_x, final_y)
    
    def __add__(self, other):
        '''
        defines + operator and returns a Point object

        '''

        #adds x coordinates and y coordinates
        return Point(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        '''
        defines - operator and returns a Point object

        '''

        #subtracts x coordinates and y coordinates
        return Point(self.x-other.x, self.y-other.y)
    
    def __eq__(self, other):
        '''
        defines == operator and returns bool object

        '''

        #returns True if points are exactly equal
        if isinstance(other, Point) == False:
            return False
        if self.x == other.x and self.y == other.y:
            return True
        
    def __ne__(self, other):
        '''
        defines != operator and returns bool object

        '''

        #returns True if points are not equal
        if self.x != other.x and self.y != other.y:
            return True



    
    
    
        

 
 
 
