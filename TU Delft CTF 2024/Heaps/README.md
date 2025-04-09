# Heaps
**Category:** Pwn
**Difficulty:** Hard

## Description
You've heard of binary heaps, binomial heaps, Fibonacci heaps, leftist heaps, glibc heap... But have you heard of heaps on a heap?

## Solution
Deleting the heap leaves a dangling pointer in the array. This UAF makes it possible to leak the libc address from a big chunk that ends up in the unsorted bin if the tcache is full and then perform tcache poisoning to overwrite `__free_hook` with the address of `system`.