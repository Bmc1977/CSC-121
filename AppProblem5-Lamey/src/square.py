from graphics import Rectangle, Point

class Square(Rectangle):
    '''
        Extends the functionality of the Rectangle class to allow for the 
        specific creation of a Square.

        For parent classes I considered _BBox, Rectangle, Polygon, 
        and GraphicsObject. I chose to go with Rectangle because a 
        square seemed the most closely related to a Rectangle. I also
        believe that it will lead to the least amount of duplicate code.
    '''

    def __init__(self, p1, side_length):
        '''
            : param p1: lower-left point of the square.
            : param side_length: side-length of the square.
        '''
        self.p2 = Point(p1.x + side_length, p1.y + side_length)
        super().__init__(p1, self.p2)
        self.side_length = side_length

    def __repr__(self):
        '''
        : return: A string representation of the square object.
        '''
        return "Square({}, {})".format(str(self.p1), str(self.p2))

    def clone(self):
        '''
            : return: Returns a copy of the dotted line object.
        '''
        other = Square(self.p1, self.side_length)
        other.config = self.config.copy()
        return other

    def _draw(self, canvas, options):
        '''
            Draws the square to the screen.
            : param canvas: the canvas to draw the square to.
            : param options: options for how to draw the square.

            : return: A square object to be drawn to the screen
        '''
        p1 = self.p1
        p2 = self.p2
        x1,y1 = canvas.toScreen(p1.x,p1.y)
        x2,y2 = canvas.toScreen(p2.x,p2.y)
        return canvas.create_rectangle(x1,y1,x2,y2,options)

    def clone(self):
        '''
            Returns a copy of the square object.
            : return: Square copy
        '''
        other = Rectangle(self.p1, self.p2)
        other.config = self.config.copy()
        return other