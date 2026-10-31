from z3 import *

def is_letter(n):
  # TODO: Implement a check for whether n is a letter (a-z)
  # Keep in mind: `n` is a Z3 integer.
  return And(n >= ord('a'), n <= ord('z'))

def is_space(n):
  # TODO: Implement a check for whether n is a space (32)
  # Keep in mind: `n` is a Z3 integer.
  return n == ord(' ')

def solve(vars, constraints):
  s = Solver()
  s.add(constraints)
  if s.check() == sat:
    m = s.model()
    return "".join(chr(m[v].as_long()) for v in vars)
  return None

oracle = 0x15579fc44eb12487e9e2ff5b80bd040c5

# TODO: Complete the challenge here.

for N in range(0, 31):
  vars = []
  constraints = []
  
  # TODO: Complete the challenge here.
  
  # Create a Int variable for each character, and require that each of them is either
  # a space or a letter
  for i in range(N):
    v = Int(f"v{i}")
    vars.append(v)
    
    c = Or(is_space(v), is_letter(v))
    constraints.append(c)
  
  if N > 5:
    # If there are five consecutive letters, then the next one must be a space.
    for i in range(N - 5):
      five_consecutive_letters = And(
        is_letter(vars[i]),
        is_letter(vars[i + 1]),
        is_letter(vars[i + 2]),
        is_letter(vars[i + 3]),
        is_letter(vars[i + 4])
      )
      constraints.append(Implies(five_consecutive_letters, is_space(vars[i + 5])))
  
  # Now compute the checksum and constrain that the checksum equals the target
  checksum = 0x1505
  for v in vars:
    checksum = checksum * 33 + v
  
  constraints.append(checksum == oracle)
  
  # The following code runs the solver and returns the first solution found
  result = solve(vars, constraints)
  if (result is not None):
    print(result)
    break
