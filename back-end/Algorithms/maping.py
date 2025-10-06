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

t = trt.Turtle()
screen = trt.Screen()

def teleport(handle, target_location):
    t = handle
    t.penup()
    t.goto(target_location)
    t.pendown()

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
    def __init__(self, coordinate_list, connections):
        self.coordinate_list = coordinate_list
        self.connections = connections
        print("Visualisation tool is starting")

    def init_map(self):
        '''
        Making maps initialisation such that no two nodes interfeer and makes sense of random ness
        - Go through the coordinates list and plot them first
        - iterate pairs and connect them
            '''
        for cord in self.coordinate_list:
            teleport(t, cord) # TODO target location changed
            t.dot(5)
        # Making connections of the pairs
        for con in self.connections:
            print(f'Debug information : {con[0]} and one more : {con[1]}')
            # TODO Fix this pipeline | thing working with ipython3
            if len(con[]) == 2:
                t.goto(con[0])
                t.goto(con[1])
                
            else:
                print(f"I think data pipeline is brokem : {con}")
            
        print("Map Initialised")

# Map initiating numbers
def random_pick(l):
    r = random.randint(0, len(l) - 1)
    return l[r]


def map_generate(generation_limit=10):
    '''
    input : number of pairs to make 
    return : Cords and randomised pairs set to mapout
    
    Cords generation
    - Non repetitive and random > make history of generated pointim
    - Spreaded into the mid of graph > Make them in boundary of generatio
    
    Pairs generation
    > Make least disconnection for simplicity atleast make some sort of interconnection 
        ~ Make first layer of connection to connect every point 
        ~ Layers of multiconnection is randomised
    '''
    generate = True
    generated_cords = []
    limmit = (-500,500)
    while generate:
        x = random.randint(-100,100)
        y = random.randint(-100, 100)
        element = (x,y)
        if not(element in generated_cords):
            generated_cords.append(element)  # adding cords
            if len(generated_cords) == 10:
                generate = False  # Breaking loop 
    print(f'Cords generated : {generated_cords}')

    # first layer highway connection ** Color coding could be good 
    i = 0
    pair_list = []  # list of tuples 
    while i <= (len(generated_cords) - 1):
        pair_list.append((generated_cords[i],generated_cords[i + 1]))
        i += 2

    # Taking randomised pairs from the base pairing
    layer = random.randint(2,10)
    for iteration in (0,layer):
        p1 = random_pick(pair_list)
        p2 = random_pick(pair_list)
        elem = [p1, p2]
        if not(elem in pair_list):
            pair_list.append(elem)
    print(f'Final check : {generated_cords, pair_list}')

    return generated_cords, pair_list # final return

a ,b = map_generate()

v = Visualisation(a, b)
v.init_map()



screen.exitonclick()
