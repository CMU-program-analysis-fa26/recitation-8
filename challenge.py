from z3 import *

def checksum(s):
  v = 0x1505
  for char in s:
    v = (v * 33) + ord(char)
  return v

def is_letter(n):
  # TODO: Implement a check for whether n is a letter (a-z)
  return True

def is_space(n):
  # TODO: Implement a check for whether n is a space (32)
  return True

oracle = 0x15579fc44eb12487e9e2ff5b80bd040c5

for N in range(0, 31):
  vars = []
  constraints = []
  
  # TODO: Complete the challenge here.
  
  # The following code runs the solver and returns the first solution found
  s = Solver()
  s.add(constraints)
  if s.check() == sat:
    m = s.model()
    result = "".join(chr(m[v].as_long()) for v in vars)
    print(result)
    break
