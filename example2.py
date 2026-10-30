"""
Use Z3 to solve the following system:
0 < x < 10
0 < y < 10
x * x + 1 = y - 2
"""


from z3 import *

x = Int('x')
y = Int('y')

constraints = () # TODO: fill in the constraints here

solve(*constraints)