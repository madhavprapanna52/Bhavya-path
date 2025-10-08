"""
Algorithm for shared transportation system
Features 
 - graphical visualisation
 - Making different algorithms for the graph nodes

 Procedure

    - Initialise random cordinates as places
    - Init random people and a random location for them to reach
    - Make routes optimised with minimum distance for all shared via route
"""
from Graph import *
import turtle

t = turtle.Turtle()
s = turtle.Screen()

# Basic turtle config
s.bgcolor("black")
s.title("Bhavyapath")


g = Graph(t)
g.plot_cords(100, 500)



s.exitonclick()
