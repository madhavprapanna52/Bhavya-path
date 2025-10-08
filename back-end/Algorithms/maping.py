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
import math 
import turtle as trt 
import random

t = trt.Turtle()
screen = trt.Screen()

# turtle config
t.hideturtle()
screen.bgcolor("black")
t.pencolor("white")
t.speed(100)

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
    def __init__(self, coordinate_list):
        self.coordinate_list = coordinate_list
        print("Visualisation tool is starting")

    def init_map(self):
        '''
        Making maps initialisation such that no two nodes interfeer and makes sense of random ness
        - Go through the coordinates list and plot them first
        - iterate pairs and connect them
            '''
        for cord in self.coordinate_list:
            teleport(t, cord) # TODO target location changed
            t.pencolor("red")
            t.dot(10)
        # Making connections of the pairs
        print("Map Initialised")

    # TODO Make this execution algorithm work with any sort of algorihtm it wont work with required
    def show_connections(self, mesh_list):
        print(f'Mesh list for debuging : {mesh_list}')
        mesh_key_list = list(mesh_list.keys())
        for point in mesh_key_list:
            elements = mesh_list[point]
            print(f'Elements : {elements}')
            teleport(t, point)
            for node in elements:
                t.pendown()
                print(f'Node :{node}')
                # Extract them and place them
                
                t.goto(int(node[0]), int(node[1]))
                teleport(t, point)


# Map initiating numbers
def random_pick(l):
    r = random.randint(0, len(l) - 1)
    return l[r]


def map_generate(generation_limit=20):
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
    while generate:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        element = (x,y)
        if not(element in generated_cords):
            generated_cords.append(element)  # adding cords
            if len(generated_cords) == generation_limit:
                generate = False  # Breaking loop 
    print(f'Cords generated : {generated_cords}')

    # first layer highway connection ** Color coding could be good 
    i = 0
    pair_list = []  # list of tuples 
    while i <= (len(generated_cords) - 1):
        pair_list.append((generated_cords[i],generated_cords[i + 1]))
        i += 2
    return generated_cords

# Making new path initialisatoin algorithm via finding path measures
# TODO Path initialisation doesnt works it have to be modified such that it can sustain to make modification

a = map_generate()  # updated map generation thing just makes map cords only

# Distance based finding logic
def dis(p1, p2):
    b = p2[0] - p1[1]
    p = p2[1] - p1[1]
    return math.sqrt((b ** 2) + (p ** 2)) # distance


# Making coords connection via generated coordinates
def generate_roads_mesh(cords_list):  # working fine i guess
    """
    Makes connections of the points via connecting them interchangebility with respect to the distance to form the graph node with weights of distance and computing cost of the distance with respect to the fuel cost * distances 

    Application 
        1. Using to make the initial roads blocks and mesh to set things with weights of distances -- computed at Execution
        2. Finding best routes wrt number of people want to go  to a destination and paths possible with path having minimum costumer
    """
    final_mesh = {} # list of pared tuples for mesh
    for point in cords_list:
        final_mesh[point] = [] # list of points
        distance_dict = {} # distance : point --> for final retrival
        cords_list.remove(point)
        for p in cords_list:
            dist = dis(point, p) # Distance Finding
            distance_dict[dist] = p

        # Picking up nearby points
        distances = list(distance_dict.keys())
        lim = 0
        print(f'Debug information: {distances}')
        for distance in distances:
            if (distance == min(distances)):
                print(distance)
                final_mesh[point].append(distance_dict[distance])
                distances.remove(distance)
                lim += 1
    return final_mesh  # returns the final disctionary

    

v = Visualisation(a)
v.init_map()

mesh = generate_roads_mesh(a)
v.show_connections(mesh)


screen.exitonclick()
