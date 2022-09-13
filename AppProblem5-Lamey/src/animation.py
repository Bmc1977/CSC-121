from tkinter.tix import MAIN
from graphics import *
from dottedline import DottedLine
from square import Square
from arc import Arc
from math import sin, cos, atan, sqrt

PI = 3.1415

def move_all(shapeList, dx, dy, win):
    """ Move all shapes in shapeList by (dx, dy)."""
    for shape in shapeList:
        shape.move(dx, dy)
        point = Point(shape.getCenter().x, shape.getCenter().y)
        point.draw(win)


def move_on_line(shapeList, dx, dy, repetitions, delay, win):
    """Animate the shapes in shapeList along a line on win.
    Move by (dx, dy) each time.
    Repeat the specified number of repetitions.
    Have the specified delay (in seconds) after each repeat.
    """

    win.autoflush = False               # 1. this line allows us as programmers to control when to redraw
    for i in range(repetitions):
        move_all(shapeList, dx, dy, win)
        update()                        # 2. this says: redraw! (it's from the graphics module)
        time.sleep(delay)
    win.autoflush = True   

def calculate_radius(shape, center):
    '''
        :param shape: The shape to calculate the radius to
        :param center: The center for the radius

        :return: The calculated radius
    '''
    shape_center = shape.getCenter()
    dx = shape_center.x - center.x
    dy = shape_center.y - center.y
    return sqrt(dx ** 2 + dy ** 2)

def calculate_angle(shape, center):
    '''
        :param shape: The shape to calcluate the angle to
        :param center: The center for the angle

        :return: The calculuated angle.
    '''
    angle = 0
    if ((shape.getCenter().y-center.y) / (shape.getCenter().x-center.x) > (PI / 2)):
        angle = atan((shape.getCenter().y-center.y) / (shape.getCenter().x-center.x)) + PI
    else:
        angle = atan((shape.getCenter().y-center.y) / (shape.getCenter().x-center.x))

    return angle

def move_all_circle(shapeList, center, speed, win):
    '''
        :param shapeList: The shapes that are being moved.
        :param center: The center of the circle.
        :param speed: The speed to move around the circle.
        :param win: The window to be drawn to.
    '''
    for shape in shapeList:
        radius = calculate_radius(shape, center)
        angle = calculate_angle(shape, center)
        newAngle = angle + speed
        x = radius * cos(newAngle) + center.x
        y = radius * sin(newAngle) + center.y
        point = Point(x, y)
        point.draw(win)
        shape.move(x - shape.getCenter().x, y - shape.getCenter().y)


def move_on_circle(shapeList, center, speed, repetitions, delay, win):
    '''
        :param shapeList: The shapes that are moving
        :param center: The center that the shapes are moving around.
        :param speed: The speed at which the shapes are moving.
        :param repetitions: How many moves the shapes should make.
        :param delay: The delay between each repetition.
        :param win: The window where the shapes will be drawn.
    '''
    win.autoflush = False              
    for i in range(repetitions):
        move_all_circle(shapeList, center, speed, win)
        update()
        time.sleep(delay)
    win.autoflush = True 

def fill_list(center, win):
    '''
        Creates the list for my animation
    '''
    circle = Circle(center, 20)
    square = Square(Point(center.x-10, center.y-10), 20)
    circle.draw(win)
    square.draw(win)
    return [circle, square]

def main():
    win = GraphWin("My Animation", 400, 400)
    win.setBackground("white")
    win.yUp()
    my_list = fill_list(Point(100, 100), win)
    for i in range(10):
        move_on_line(my_list, 20, 0, 1, 0.1, win)
    move_on_circle(my_list, Point(200, 200), (PI / 64), 10, 0.3, win)
    for i in range(15):
        move_on_line(my_list, 0, 10, 1, 0.1, win)

    for i in range(8):
        move_on_line(my_list, -20, 0, 1, 0.1, win)

    move_on_circle(my_list, Point(0, 400), (PI / 64), 10, 0.3, win)

    for i in range(4):
        move_on_line(my_list, -20, 0, 1, 0.1, win)

    for i in range(30):
        move_on_line(my_list, 0, -10, 1, 0.1, win)

    d1 = DottedLine(Point(100, 100), Point(300, 300))
    d2 = DottedLine(Point(100, 300), Point(300, 100))
    d1.draw(win)
    d2.draw(win)

    a = Arc(Point(100, 200), Point(300, 300), 180, 180)
    a.draw(win)

    win.getMouse() # Pause to view result
    win.close()


if __name__ == '__main__':
    main()