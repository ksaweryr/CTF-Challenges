# Branchless Programming
**Category:** Reversing
**Difficulty:** Hard

## Description
I've heard that branchless programming makes your code go brrr... very fast - so I decided to speed up some of my Python code.

## Solution
Figure out that everything boils down to encrypting the flag with a one-time pad, hook the `reduce` operation to see the values passed to `__xor__` and `__eq__` operators.