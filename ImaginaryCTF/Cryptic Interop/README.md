# Cryptic Interop
**Category:** Reversing
**Difficulty:** Hard

## Description
Did someone order some French gaufres? I've collaborated with my friends to deliver it to you as fast as possible!

## Solution
Extract `libinterop.so.enc` from the jar and decrypt it using the algorithm from the `apply` method in the `Main` class. Next analyse this shared library and realize that it encrypts the input using textbook RSA and compares it to a constant number. Finally decrypt the modulus of the RSA key, use Sage or [http://factordb.com/](http://factordb.com/) to find out the primes (one of them is very small, so it's easy to factor this number) and decrypt the flag.