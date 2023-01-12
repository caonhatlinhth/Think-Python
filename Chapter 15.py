import math
import copy
from world import world

class point(object):
    """Represents a point in 2-D space."""

point1 = point()
point2 = point()

point1.x, point1.y = 1.0, 2.0
point2.x, point2.y = 3.0, 4.0


def distance_between_two_point(point1, point2):
    """Return the distance between 2 points"""
    distance_x = point1.x - point2.x
    distance_y = point1.y - point2.y
    return math.sqrt(distance_x**2 + distance_y**2)

class rectangle(object):
    """Represents a rectangle
    
    attributes: width, height, corner
    """

box = rectangle()
box.width = 100
box.height = 200
box.corner = point()
# box.corner.x = 0.0
# box.corner.y = 0.0
box.corner.x = 50
box.corner.y = 50

def find_center(rectangle):
    p = point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y + box.height/2.0
    return p

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def print_point_center():
    blank = point()
    # blank.x = 3
    # blank.y = 4
    blank.x = 0
    blank.y = 0

    new_point = point()
    new_point.x = 3
    new_point.y = 4
    # center = find_center(box)
    # print_point(center)
    print(distance_between_two_point(new_point, blank))

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
    # print(box.width)
    # print(box.height)

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    # print(rect.corner.x)
    # print(rect.corner.y)

def move_rectangle_copy(rect, dx, dy):
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)
    return new

def main():
    # print("The distance between 2 points is %g" % distance_between_two_point(point1, point2))
    # print_point_center()
    # grow_rectangle(box, 50, 100)
    # move_rectangle(box, 50, 100)
    new_box = move_rectangle_copy(box, 50,100)
    print(new_box.corner.x)
    print(new_box.corner.y)
    
    pass

if __name__ == "__main__":
    main()