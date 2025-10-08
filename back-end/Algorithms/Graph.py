"""
Responsible for making graphical visualisation and debuging algorithms

features 
    - Simple ploting tool with turtle 
    - Mesh making unit
"""
import random
import math


def random_point(cords_range):
    x = random.randint(-cords_range, cords_range)
    y = random.randint(-cords_range, cords_range)
    return (x,y)

def distance(src, trgt):
    dx = trgt[0] - src[0]
    dy = trgt[1] - src[1]
    distance = math.ceil(math.sqrt((dx ** 2) + (dy ** 2)))
    return distance


class Graph:
    '''
    Graphing tool
    input : turtle handle from main, Basic graph configurations
    output : Makes graphs and plots algorithm step by step
    '''
    def __init__(self, turtle_handle):
        self.t = turtle_handle
        print("Graph started")

    def plot_cords(self, limit_points=10, cords_range=300):
        t = self.t
        cordinates = self.init_cords(limit_points, cords_range)
        for point in cordinates:
            t.penup()
            t.goto(point)
            t.pendown()
            t.pencolor("yellow")
            t.dot(5)

    def init_cords(self, limit_points, cords_range):
        """
        Initialisation of coordinates
        output : [()]
        """
        points = []
        squish = 50 # Parameter controlls the congesiton of points
        points.append(random_point(cords_range)) # initialisation
        for i in range(0, limit_points):
            unique = False
            while not(unique):
                point = random_point(cords_range)
                if (point in points) or (distance(points[-1], point) > squish) or (distance((0,0), point) > 300):
                    unique = False 
                else:
                    points.append(point)
                    unique = True 
        for i in points:
            print(f'Point : {i}')
        return points
