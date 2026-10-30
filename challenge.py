from z3 import *

def is_letter(n):
  # TODO: Implement a check for whether n is a letter (a-z)
  # Keep in mind: `n` is a Z3 integer.
  return None

def is_space(n):
  # TODO: Implement a check for whether n is a space (32)
  # Keep in mind: `n` is a Z3 integer.
  return None


"""
Solves a set of constraints over Z3 integer variables representing characters.

Outputs
  A string representing the solution if one exists, otherwise None.
"""
def solve(vars, constraints):
  s = Solver()
  s.add(constraints)
  if s.check() == sat:
    m = s.model()
    return "".join(chr(m[v].as_long()) for v in vars)
  return None

oracle = 0x15579fc44eb12487e9e2ff5b80bd040c5

# TODO: Complete the challenge here. You should call is_letter, is_space, and solve (potentially multiple times).