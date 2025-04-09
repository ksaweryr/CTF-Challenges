# The PIE is a Lie
**Category:** Pwn
**Difficulty:** Easy

## Description
My binary is position-independent, it uses address space layout randomization, there's no way you can find the address of my shell function!

## Solution
Option 3 leaks the address of `get_answer`. Option 1 can be used to overwrite the return address of `main`.