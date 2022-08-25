from math import pi
circ = []

def circle():
    diameter = int(input("What is the diameter of the circle?"))
    circumference = pi*diameter
    circ.append(circumference)
    print(circ)

circle()