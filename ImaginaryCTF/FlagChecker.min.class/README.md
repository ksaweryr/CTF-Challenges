# FlagChecker.min.class
**Category:** Reversing
**Difficulty:** Hard

## Description
I have realised that the .class file with my flag checker is bloated. Why do I need the constant pool and stuff, when I can store only the actual code?

Hint: `([B)Z`

## Solution
Create a class file with a function that takes an array of bytes and returns a boolean with code that's exactly as many bytes long as the code provided in the attachment (e.g. using Krakatau2). Replace the stub code with the code from the attachment and open the class file in a Java decompiler. Solve system of equations. (e.g. using Z3). Reference scripts to forge the class file and to calculate the flag: [forge.py](./src/forge.py), [solve.py](./src/solve.py)