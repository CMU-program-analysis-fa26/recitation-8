# Set up

Make a fork of this repository.

## Create a Python virtual environment

First, create a virtual environment to isolate the dependencies:

```bash
python3 -m venv venv
```

Then activate the virtual environment:

```bash
source venv/bin/activate
```

## Install z3-solver

Install the Z3 solver Python interface:

```bash
pip install z3-solver
```

If the installation is successful you should be able to run `python3
example1.py`, which solves the equation `x ** 2 + 3 = 228` for integer `x`. It should output either `15` or `-15`.

# Tasks #1 & #2
Here are the contents of `example1.py`:

```python
"""
Goal: Solve for the equation x ** 2 + 3 = 228, for integer values of x
"""

# First we import z3
from z3 import *

# Next we declare the variable x as an integer
# This is a symbolic variable, whose value will be determined by the solver
x = Int("x")

# Now we define the constraint that represents the equation we want to solve
constraint = x * x + 3 == 228

# Finally, we ask the solver to find a solution that satisfies the constraint
solve(constraint)
```

This declares an Z3 `Int` constant named `x`, creates a constraint that requires `x * x + 3 = 228` to hold, and then calls the solver to find a solution.

## Task #1

If your result of running `python3 example1.py` is positive, then can you add a constraint to force the output to be negative? If your result is negative, can you add a constraint to force the output to be positive?

## Task #2

Modify the constraint(s) to become unsatisfiable (non-trivially), and then try running the solver again.

# Task #3

Complete `example2.py` to solve the following system:
```
0 < x < 10
0 < y < 10
x * x + 1 = y - 2
```
in integers.

# Task #4: Challenge

You will complete this task in `challenge.py`.

Here is some code that computes a checksum of a string `s` (also implemented in `checksum.py`):

```python
def checksum(s):
  v = 0x1505
  for char in s:
    v = (v * 33) + ord(char)
  return v
```

Your job is to find a string (using z3) that satisfies the checksum
`0x15579fc44eb12487e9e2ff5b80bd040c5`. Specifically, your string should cause the following to be
true:

`checksum(SOLUTION) == 0x15579fc44eb12487e9e2ff5b80bd040c5`

**Don't brute force it, that will take too long.**

The set of possible characters are `a-z` (ASCII 97-122) and spaces (ASCII 20). The string has length at most 30, and there are no words (consecutive letters) that are more than five letters. (Think about how this can be implemented as logical formulas.)

<details>
<summary>Hint #1</summary>

You are allowed to create multiple instances of the solver and run different Z3 instances in your `challenge.py`. This could be useful trying out different lengths.

</details>

<details >
<summary>Hint #2</summary>

`Implies` may be useful for enforcing that there are no words more than 5 letters.
</details>


Have fun!

# References

- [Python Z3 examples](http://ericpony.github.io/z3py-tutorial/guide-examples.htm)
- [Python API](http://z3prover.github.io/api/html/namespacez3py.html)
- [Programming Z3, a guide](http://theory.stanford.edu/~nikolaj/programmingz3.html)
