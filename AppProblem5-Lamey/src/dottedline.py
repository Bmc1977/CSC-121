from graphics import Line, Point
from math import atan, cos, sin

class DottedLine(Line):
    '''
        Extends the functionality of the Line class to allow for the 
        creation of a dotted line. Each of the "dashes" on the dotted
        line are 10px long.
    '''

    def __init__(self, p1, p2):
        '''
            : param p1: End point of the dotted line.
            : param p2: Other end point of the dotted line.
        '''
        super().__init__(p1, p2)

    def __repr__(self):
        '''
            : return: a string representation of the dotted line object.
        '''
        return "Dotted Line({}, {})".format(str(self.p1), str(self.p2))

    def clone(self):
        '''
            : return: Returns a copy of the dotted line object.
        '''
        other = DottedLine(self.p1, self.p2)
        other.config = self.config.copy()
        return other

    #TODO Finish Dotted Line (Every 5 Pixels)
    def _draw(self, canvas, options):
        '''
            Draws the dotted line to the canvas provided.

            : param canvas: The canvas object to be drawn to.
            : param options: Options for how the dotted line should be drawn
            
            : return: A dotted line object to be drawn to the screen
        '''
        p1 = self.p1
        p2 = self.p2
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        return canvas.create_line(x1,y1,x2,y2, options, dash=(4, 2))