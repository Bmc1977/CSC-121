"""Simple animation of a group of objects making a face.
"""

from graphics import update, Circle, Line, Oval, Point, GraphWin
import time


def move_all(shape_list, dx, dy):
    """ Move all shapes in shapeList by (dx, dy)."""
    for shape in shape_list:
        shape.move(dx, dy)


def move_on_line(shape_list, dx, dy, repetitions, delay, win):
    """Animate the shapes in shapeList along a line on win.
    Move by (dx, dy) each time.
    Repeat the specified number of repetitions.
    Have the specified delay (in seconds) after each repeat.
    """

    win.autoflush = False               # 1. this line allows us as programmers to control when to redraw
    for i in range(repetitions):
        move_all(shape_list, dx, dy)
        update()                        # 2. this says: redraw! (it's from the graphics module)
        time.sleep(delay)
    win.autoflush = True                # 3. give redraw-control back to "the system"


def make_face(center, win):
    """display face centered at center in window win.
    Return a list of the shapes in the face.
    """

    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1_center = center.clone()  # face positions are relative to the center
    eye1_center.move(-10, 5)  # locate further points in relation to others
    eye1 = Circle(eye1_center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2_end1 = eye1_center.clone()
    eye2_end1.move(15, 0)
    eye2_end2 = eye2_end1.clone()
    eye2_end2.move(10, 0)

    eye2 = Line(eye2_end1, eye2_end2)
    eye2.setWidth(3)
    eye2.draw(win)

    mouth_corner1 = center.clone()
    mouth_corner1.move(-10, -10)
    mouth_corner2 = mouth_corner1.clone()
    mouth_corner2.move(20, -5)

    mouth = Oval(mouth_corner1, mouth_corner2)
    mouth.setFill("red")
    mouth.draw(win)

    return [head, eye1, eye2, mouth]


def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.yUp()  # make right side up coordinates!

    face_list = make_face(Point(40, 100), win)  # create 'basic' face centered at (40,100)

    # set up parameters for animation
    steps_across = 46
    dx = 5
    dy = 3
    wait = .04

    # move face around in a triangle (three lines)

    for i in range(3):
        move_on_line(face_list, dx, 0, steps_across, wait, win)
        move_on_line(face_list, -dx, dy, steps_across // 2, wait, win)
        move_on_line(face_list, -dx, -dy, steps_across // 2, wait, win)

    # once animation is complete, let user click to close

    win.promptClose(win.getWidth() / 2, 20)


if __name__ == "__main__":
    main()
