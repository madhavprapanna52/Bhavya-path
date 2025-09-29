"""
Making path finding algorithm

Features
    1. Adding destination as nodes
    2. Finding path with emmision and cost variable constraints
    3. Taking multiple costumer for sharing route planning and cost reduction

Execution plan 
. Visualizing algorithm through turtle
. Building algorithm
. Tweeking algorhthm to finetune it

"""
import turtle as trt 
import random
from turtle_tools import *
t = trt.Turtle()
screen = trt.Screen()

# Visualisation tool
class Visualisation:
    '''
    Aim : Making visualisation of algorithm execution for debug 
    Features 
    - Initialising toy map via nodes cordinates 
    - Execution tracing of algorithm
    nodes = [cordinates list] , [list of tuples consisting connection information]| 
    '''
    # TODO Algorithm execution tracing mechanism 
    def __init__(self, nodes):
        self.coordinate_list, self.connections = nodes
        print("Visualisation tool is starting")

    def init_map(self):
        '''
        Making maps initialisation such that no two nodes interfeer and makes sense of random ness
        - Go through the coordinates list and plot them first
        - iterate pairs and connect them
        '''
        for cord in self.coordinate_list:
            teleport(t, target_location)
            t.dot(5, color="red")
        # Making connections of the pairs
        for con in self.connections:
            teleport(t, con[0]) # source
            t.goto(con[1]) # geting to end point
            t.penup()

        print("Map Initialised")




screen.exitonclick()
