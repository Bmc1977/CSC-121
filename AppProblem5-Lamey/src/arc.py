from graphics import _BBox
import tkinter as tk

class Arc(_BBox):
    '''
        Represents an arc in 2D space that can be drawn to a canvas.

        For parent classes I considered _BBox and Oval, but decided 
        to go with _BBox because if a line's parent is _BBox I think
        Arc should stay consistent with that.
    '''

    def __init__(self, p1, p2, start_angle, amount_angle):
        _BBox.__init__(self, p1, p2)
        self.start_angle = start_angle
        self.amount_angle = amount_angle

    def clone(self):
        '''
            :return: A hard copy of the arc object.
        '''
        other = Arc(self.p1, self.p2, self.start_angle, self.amount_angle)
        other.config = self.config.copy()
        return other
   
    def _draw(self, canvas, options):
        '''
            :param canvas: The canvas that the object should be drawn to.
            :param options: Options for how to draw the object.
        '''
        p1 = self.p1
        p2 = self.p2
        start_angle = self.start_angle
        amount_angle = self.amount_angle
        x1,y1 = canvas.toScreen(p1.x,p1.y)
        x2,y2 = canvas.toScreen(p2.x,p2.y)
        return canvas.create_arc(x1,y1,x2,y2,options, start=start_angle, 
                                    extent=amount_angle, style=tk.ARC)