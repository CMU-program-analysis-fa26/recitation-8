"""
Goal: Solve for the equation x ** 2 + 3 = 228, for integer values of x
"""

# First we import z3
from z3 import *

# Next we declare the variable x as an integer.
# This is a symbolic variable, whose value will be determined by the solver.
x = Int("x")

# Now we define the constraint that represents the equation we want to solve.
# Notice that the equality operator `==`, the arithmetic operators like `+` and `*` are all overloaded in Z3.
constraint = x * x + 3 == 228

# Finally, we ask the solver to find a solution that satisfies the constraint.
solve(constraint)



# Task 1a: If your result of running `python3 example1.py` is positive, then can you add a constraint to force the output to be negative? If your result is negative, can you add a constraint to force the output to be positive?

# Task 1b: Modify the constraint(s) to be unsatisfiable (non-trivially). Try running the solver again.