# SVM Revenge
**Category:** Reversing
**Difficulty:** Medium/Hard

## Description
As foretold, the revenge of SVM from round 46 is here!

## Solution
Figure out that the VM uses a queue to perform all operations. Reverse-engineer the VM's bytecode and figure out that for each block of 16 characters it generates 16 linear equations mod 256. Solve the system of equations for each block to recover the flag.
